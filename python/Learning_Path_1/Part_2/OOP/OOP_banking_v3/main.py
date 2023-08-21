#! python3
# pylint: disable=pointless-string-statement


# import modules
from getpass import getpass
import datetime
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os
import pickle
import random



"""
TODO:

Bug fixes around DataFrames, transaction logging / history and transaction visualizations.
- Refactor beginning from the initial DataFrame initializations and reading CSV standards on the account level, then work your way up to the customer level.
- Currently, there are too many DataFrames being instantiated and written over in different steps / processes.

There is also another issue with XYZ and creating directory in home dir and not cwd.
"""



#################################################################################
##############################  Bank CLASS  #####################################
#################################################################################

class Bank:
    def __init__(self, name):
        self.name = name
        
        # check if there is already a directory with the name in current dir,
        # if not create one and its sub directories when the bank is initiated for the first time
        self.path = f'{os.getcwd()}/{name}'
        self.customers_path = self.path + os.path.sep + "customers"
        self.accounts_path = self.path + os.path.sep + "accounts"

        if not os.path.exists(self.path):
            os.mkdir(self.path)
            os.mkdir(self.customers_path)
            os.mkdir(self.accounts_path)
        

    def reconcile(self):
        with open(self.path, 'wb') as f:
            pickle.dump(self, f)


    ### customer methods ### 
    # create customer
    def create_customer(self):
        """
        # create new customer - needs to have dialogue to create new randomized encryption key (enter PIN and encrypts it)

        To do's:
        >> encrypt
        >> rng for customer_id
        >> check for duplicates so that data does not get corrupted / overwritten
        """

        # take in customer input to create a new user account
        print("Please enter your name\n")
        customer_name = input(">> ")

        print("Please enter your address\n")
        customer_address = input(">> ")

        print("Please enter your four digit PIN\n")
        customer_pin = input(">> ")

        # randomly generate a customer ID and create the customer path + check for duplicates
        customer_id = str(random.randint(1000000000, 9999999999))
        while os.path.exists(f"{self.customers_path}{os.path.sep}{customer_id}.pkl"):
            customer_id = str(random.randint(1000000000, 9999999999))
        
        print(f"Your new Customer ID is {customer_id}, please write this down as you will need it for logging into your account")
        # create the object
        new_customer = Customer(customer_name, customer_address, customer_id, customer_pin, self.path)
        new_customer.create_account()

        # save the object in self.path
        with open(self.customers_path + f'{os.path.sep}{customer_id}.pkl', 'wb') as f:
            pickle.dump(new_customer, f)

    ## account related methods ##
    # delete existing customer
    # change customer information
    # authenticate customer / access information



    def create_account(self, target_customer_id):
        """
        To do's:
        Eventually, it needs to check for existing account IDs in the database to
        make sure that they don't exist already so as to not overwrite.
        """
        # open / access the target customer object (evnetually with authenticate / login)
        # call the create account method for the customer object
        with open(f"{self.customers_path}{os.path.sep}{target_customer_id}.pkl", 'rb') as f:
            customer_object = pickle.load(f)
            customer_object.create_account()
        



    def authenticate(self):
        """
        Bank.Authenticate() prompts for the user ID, and password and tries to authenticate them.
        Every loop they must enter their username, and then their PIN.
        In the first version, authenticate will just check PIN entered = PIN.
        In later versions, all user files created will be encrypted with thier PIN, and therefore, the data can only be decrypted
        if the entered PIN is correct. So that the objects are not simply readable as they are in encrypted binary format.
        """

        # request for credentials
        cid = input("Please enter your Customer ID")
        pin = getpass("Please enter your 4 digit PIN number:")

        
        if not os.path.exists(f"{self.customers_path}{os.path.sep}{cid}.pkl"):
            print(f"Invalid Credentials: Customer does not exist at {self.customers_path}{os.path.sep}{cid}.pkl")
            return None # parent method will call this method again

        else:
            with open(f"{self.customers_path}{os.path.sep}{cid}.pkl", 'rb') as f:
                customer_object = pickle.load(f)
                
                # check credentials - if passed
                if (cid, pin) == (customer_object.cid, customer_object.pin):
                    print(f'Welcome {customer_object.name} you are now logged in.')
                    return customer_object
                # otherwise
                print("Invalid credentials: Please check Customer ID and PIN combinations again")
                return None


    def close_account(self, customer):
        # check length of number of accounts
        if len(customer.accounts) < 2:
            print(f"You currently are holding one account with {self.name}, in order to close your accounts out fully with us, please select Delete Account from options")
            return
        
        # dictionary to contain options for customers to choose from
        options = {"x": "close"}

        # list out all of the accounts available to the customer
        for idx in list(range(len(customer.accounts))):
            print(f"{idx}. ID:{customer.accounts[idx]} // Balance:{customer.check_account(customer.accounts[idx])}") 
            options[f"{idx}"] = f"{customer.accounts[idx]}"

        # select one among valid options, loop while or X to cancel
        closing_account_idx = input("Please choose an account to close:")
        while closing_account_idx not in options.keys():
            closing_account_idx = input("Please choose an account to close:")
            for key, value in options.items():
                print(f"{key}. {value}")
        if closing_account_idx.lower() == "x":
            return
        
        # select one of the valid options, that is NOT the closing account selection;
        invalid_option = options.pop(f"{closing_account_idx}")

        destination_account_idx = input("Please choose a destination account to deposit remaining funds to:")
        for key, value in options.items():
            print(f"{key}. {value}")

        while destination_account_idx not in options.keys():
            destination_account_idx = input("Please choose an account to close:")
            for key, value in options.items():
                print(f"{key}. {value}")
        
        print(customer.accounts[int(closing_account_idx)], customer.accounts[int(destination_account_idx)])

        # confirm deletion and procedure, if not, return as well
        while True:
            confirm = input("Please type \"confirm\" to proceed, and X to exit out")
            if confirm.lower() == 'confirm':
                customer.close_account(customer.accounts[int(closing_account_idx)], customer.accounts[int(destination_account_idx)])
                return
            if confirm.lower() == "x":
                return
    


    def close_customer(self, customer):
        # confirm with the user that they want to remove everything
        while True:
            confirm = input("You are about to delete your whole entire account type \"confirm\" to proceed, and X to exit out")
            if confirm.lower() == 'confirm':
                break
            if confirm.lower() == "x":
                return
        
        closed_accs_total = 0
        # loop through every single account that they have and delete it and transfer the account balance
        for account_id in customer.accounts:
            closed_accs_total += customer.check_account(account_id)
            os.remove(f"{self.accounts_path}{os.path.sep}{account_id}.pkl")
        os.remove(f"{self.customers_path}{os.path.sep}{customer.cid}.pkl")
        return True

    def forgot_password(self):
        # encryption will disable this, likely, the PIN number continues to remain accessible for the customer, however, the important customer details
        # and transaction history becomes unavailable through encryptio .
        customer_id = input("Please enter your Customer ID: ")

        # check that the customer_id exists:
        if not os.path.exists(f"{self.customers_path}{os.path.sep}{customer_id}.pkl"):
            print(f"Invalid Credentials: Customer does not exist at {self.customers_path}{os.path.sep}{customer_id}.pkl")
            return None # parent method will call this method again
        
        # if it exists, pass the object to customer
        with open(f"{self.customers_path}{os.path.sep}{customer_id}.pkl", 'rb') as f:
            customer = pickle.load(f)

            # randomly generate a OTP code
            otp_code = str(random.randint(100000, 999999))
            # send / display the OTP code (eventually, this will be sent to an email address and to a phone number using Twilio API)
            print(otp_code)

            # receive input from user
            while True:
                entered_otp = input("Please enter the 6 digit OTP sent to your email and phone number saved:")

                # if the OTP is correct, then ask to change the pin, and change the pin number + reconcile
                if entered_otp == otp_code:
                    # take in the new PIN from user, 4 digits only.
                    new_pin = input("Please enter your new 4 digit PIN number")
                    while not new_pin.isdigit() and len(new_pin) == 4:
                        new_pin = input("Please enter your new 4 digit PIN number")

                    # when it is done, change the PIN number for the customer, reconcile the customer object and then return the function to exit
                    customer.pin = new_pin
                    customer.reconcile()
                    return

                # display the incorrect options and handle them accordingly
                option_chosen = input("To resend the OTP, enter \"resend\" or to cancel out, enter \"x\"")
                # if they want to exit, press x to cancel and return
                if option_chosen.lower() == "x":
                    return None
                if option_chosen.lower() == "resend":
                    otp_code_new = str(random.randint(100000, 999999))
                    otp_code = otp_code_new
        



#################################################################################
############################  Customer CLASS  ###################################
#################################################################################


class Customer:
    """
    Customer objects are accessed by the user, through the banking UI.
    They are stored as pickle files and their methods / functions can only be accessed if the PIN they entered is correct
    Eventually, all of their files will be encrypted and in order to unlock them, you would need to enter the correct PIN
    >> To Do's
    > get total account sum / accounts overview

    """
    def __init__(self, name, address, cid, pin, bank_path):
        # key attributes
        self.name = name
        self.address = address
        self.accounts = [] # accounts is a list of strings that stores account_IDs associated with this customer, at init it is empty
        self.cid = cid
        # PIN should be an encrypted result so that the raw object saved does not contain the actual PIN but an encrypted version
        self.pin = pin

        # path variables for customer object
        self.bank_path = bank_path
        self.path = f"{bank_path}{os.path.sep}customers{os.path.sep}{cid}.pkl"
        self.accounts_path = f"{bank_path}{os.path.sep}accounts"
    
    #### METHODS ####

    def reconcile(self):
        """
        customer.reconcile()
        - opens self.path and dumps itself into the path.
        """
        with open(self.path, 'wb') as f:
            pickle.dump(self, f)
    
    
    # create new account
    def create_account(self):
        
        # randomly generate a new account ID
        new_account_id = str(random.randint(1000000000, 9999999999))
        while os.path.exists(f"{self.accounts_path}{os.path.sep}{new_account_id}.pkl"):
            customer_id = str(random.randint(1000000000, 9999999999))

        # append account ID to self accounts
        self.accounts.append(new_account_id)

        # create the new account object
        new_account = Account(new_account_id, self.bank_path)

        # save the account in the right directory
        with open(self.accounts_path + f'{os.path.sep}{new_account_id}.pkl', 'wb') as f:
            pickle.dump(new_account, f)
        self.reconcile()
    

    # account_deposit (account, amount)
    def deposit_account(self, account_id, amount):
        # check that the account is indeed owned by this customer

        # find and open the account
        with open(f'{self.accounts_path}{os.path.sep}{account_id}.pkl', 'rb') as f:
            account_object = pickle.load(f)
            # call the deposit function on the account
            account_object.deposit(amount)

    # account_withdraw (account, amount)
    def withdraw_account(self, account_id, amount):
        # check that the account is indeed owned by this customer
        if account_id not in self.accounts:
            print (f"Account ID: {account_id} does not exist or does not belong to you, please check and try agian")
            return False

        with open(f'{self.accounts_path}{os.path.sep}{account_id}.pkl', 'rb') as f:
            account_object = pickle.load(f)
            # call the deposit function on the account
            return account_object.withdraw(amount)
    
    def check_account(self, account_id):
        with open(f'{self.accounts_path}{os.path.sep}{account_id}.pkl', 'rb') as f:
            account_object = pickle.load(f)
            return account_object.balance
    

    def close_account(self, closing_account_id, destination_account_id):
        # process the deposit / withdrawls (eventually, transfers)
        withdrawn_amt = self.withdraw_account(closing_account_id, self.check_account(closing_account_id))
        self.deposit_account(destination_account_id, withdrawn_amt)

        # delete the accounts
        closing_path = f"{self.accounts_path}{os.path.sep}{closing_account_id}.pkl"
        os.remove(closing_path)

        # remove it from itself
        self.accounts.remove(closing_account_id)
        self.reconcile()
    
    def display_accounts(self):
        """
        Displays the overview of all accounts held by a customer
        """
        accounts_to_balance = ""
        total = 0

        for account_id in self.accounts:
            with open(f"{self.accounts_path}{os.path.sep}{account_id}.pkl", 'rb') as f:
                account_object = pickle.load(f)
                total += account_object.balance
                accounts_to_balance += f'\n{account_object.account_id}: ${account_object.balance}'
        
        print(accounts_to_balance)
        print(f"\n{self.cid}: Total value ${total}")


    def change_address(self):
        # take in new address
        print("Please enter your new address:")
        new_address = input(">> ")
        print(f"Your address is now changed from:\n{self.address} to {new_address}")
        self.address = new_address        
        self.reconcile()


    def get_transactions_history(self, account_id='all'):
        """
        Gets the transaction history of an account.
        Default is all transactions from all accounts
        """
        # if the account ID is passed, get and display the transaction history for that account, if it doesn't exist.
        if account_id.lower() != "all":
            try:
                csv_path = f'{self.accounts_path}{os.path.sep}{account_id}.csv'
                df = pd.read_csv(csv_path)
                print(df)
                return
            except:
                print(f'{account_id} does not exist')
                return

        # if the account_id is "all", loop through all accounts held by a customer, combining each dataframe, sorting and then printing the sorted df
        account_id_copy = self.accounts.copy()
        account_0 = account_id_copy.pop(0)
        df = pd.read_csv(f'{self.accounts_path}{os.path.sep}{account_0}.csv')

        if len(account_id_copy) >= 1:
            for account_id in account_id_copy:
                df_temp = pd.read_csv(f'{self.accounts_path}{os.path.sep}{account_id}.csv')
                df = pd.concat([df, df_temp])
        # display / return the final result
        sorted_df = df.sort_values(by='time')
        print(sorted_df)










    def visualize_account(self, account_id):
        """
        visualizes the selected account
        """
        with open(f"{self.accounts_path}{os.path.sep}{account_id}.pkl", 'rb') as f:
            account_object = pickle.load(f)
            account_object.visualize()
        

    def visualize_customer(self):
        """
        visualizes all accounts in a bar chart
        """
        pass


    def transfer(self, source_account_id, destination_account_id, amount):
        # it SHOULD technically define multi bank features.
        # withdraw from source_id
        # self.withdraw_account(source_account_id, amount)
        # deposit to destination_id
        pass

    

        



#################################################################################
############################  ACCOUNT CLASS   ###################################
#################################################################################




class Account:
    def __init__(self, account_id, bank_path):
        # does not contain information on who owns the accounts
        self.balance = 0
        self.account_id = account_id
        self.bank_path = bank_path
        self.path = f"{bank_path}{os.path.sep}accounts{os.path.sep}{account_id}.pkl"
        self.csv_path = f"{bank_path}{os.path.sep}accounts{os.path.sep}{account_id}.csv"

        # see if csv file exists
        # if it does, load it into a pandas dataframe as part of its attributes
        if not os.path.exists(self.csv_path):
            columns = ['time', 'txid', 'account_id', 'type', 'is_transaction', 'amount', 'balance_before', 'balance_after']
            df = pd.DataFrame(columns=columns)
            df.to_csv(self.csv_path, index=False)
            
        
        # at the end of it, load the new dataframe
        # self.txlog_df = pd.read_csv(self.csv_path) => we don't really need to be reading it at creation or calling it then.
        
    


    def reconcile(self):
        """
        account.reconcile()
        -- Description --
        opens self.path and dumps itself into the path.
        -- Usage --
        """
        with open(self.path, 'wb') as f:
            pickle.dump(self, f)
        
    
    def log_transaction(self, event_type, is_transaction, amount, balance_before, balance_after):
        """
        tx_data takes in an ordered list of transaction metadata.
        time, txid are generated on thsi function.
        passed / received in is type, istx, amt, balance before, balance after
        it constructs a newrow as a pd.Series object and appends it into the dataframe
        """
        # open and read the existing csv
        df = pd.read_csv(self.csv_path)

        # get the current timestamp and format it.
        now = datetime.datetime.now()
        formatted_date = now.strftime("%d-%m-%Y")
        
        # randomly generate a txid with a combination of account AID + DATE + RNG
        random_number = str(random.randint(1000,9999))
        txid = f"{self.account_id}{formatted_date}{random_number}"
        
        # construct the row with the transaction data passed and append it to the dataframe
        account_id = str(self.account_id)
        print(df)


        new_entry = [now, txid, account_id, event_type, is_transaction, amount, balance_before, balance_after]
        df.loc[len(df)] = new_entry
        # save it to the csv to reconcile
        df.to_csv(self.csv_path, index=False)


    def deposit(self, amount):
        balance_before = self.balance
        self.balance += amount
        print(f'deposited {amount}, current balance {self.balance}')
        self.log_transaction("deposit", True, amount, balance_before, self.balance)
        self.reconcile()
        return amount
    

    def withdraw(self, amount):
        if amount > self.balance:
            print("Amount exceeds current balance")
        else:
            balance_before = self.balance
            self.balance -= amount
            self.log_transaction("withdraw", True, amount, balance_before, self.balance)
            print(f'withdrew {amount}, current balance {self.balance}')
            self.reconcile()

            return amount

    def check_balance(self):
        # print(f'Current balance: ${self.balance}')
        return(self.balance)
    
    def visualize(self):
        df = pd.read_csv(self.csv_path)
        balance_over_time = df[['time', 'balance_after']]
        balance_over_time.set_index('time', inplace=True)
        balance_over_time.plot(kind='line')
        plt.show()
        plt.clf()
        

    
    def transfer(self, target_bank, target_aid):
        pass


    










#################################################################################
##############################  UI CLASS  #######################################
#################################################################################


class UI():
    def __init__(self, bank_name):
        """
        The UI object interacts with the user to call various methods in the Bank object to provide users with 
        a clean user interface, dialogues and access.
        """
        self.bank = Bank(bank_name) # the UI object constructs an instance of the bank object based on the name of the bank

        self.dialogues = {
            # self.dialogues is a key value pair of dialogues prompts and texts accessed in methods
            "welcome": "Hello user!"
        }
        # logging path
        

    # define welcome dialogue and begin the core loop
    def begin(self):
        # print welcome dialgoue
        print(f"Welcome to {self.bank.name} Banking portal:\n\n")

        
        while True:
            response = self.baseline_options()
            if response == "exit":
                print(f"Thanks for using {self.bank.name}, see you again")
                return
            

            elif response == "login":
                # loop until there is a valid customer object that is not None => therefore logged in
                loggedin_customer = self.bank.authenticate()

                while loggedin_customer:
                # continuously loops (takes user input, carries it out) until user chooses to log out
                    loggedin_response = self.loggedin_options()
                    action_taken = self.loggedin_actions(loggedin_response, loggedin_customer)
                    
                    # check if they chose to log out
                    if loggedin_response == "log_out" or action_taken == "closed_customer":
                        break
                else:
                    pass
                
                                        

            elif response == 'create_new_acc':
                self.bank.create_customer()
            
            elif response == "forgot_password":
                self.bank.forgot_password()
    




    
    def baseline_options(self):
        """
        provides baseline options pre-logging in - creating new account, forgotten password, exit.
        """
        options = {
            "0": "exit",
            "1": "login",
            "2": "create_new_acc",
            "3": "forgot_password"
        ""}
        input_str = f"""Please select from the following: 
        0. Exit Portal
        1. Log in
        2. Create new account
        3. Forgot Password
        """

        user_input = input(input_str)
        while user_input not in options.keys():
            user_input = input(input_str)
        return options[user_input]


    
    def loggedin_options(self):
        """
        provides options post logging in
        change information, get total
        deposit, withdrawmn 
        """
        options = {
            "0": "log_out",
            "1": "deposit",
            "2": "withdraw",
            "3": "change_address",
            "4": "overview",
            "5": "open_new_acc",
            "6": "close_acc",
            "7": "close_customer",
            "8": "get_transactions",
            "9": 'visualize_account'

            # "9": "transfer",

        ""}
        input_str = f"""Please select from the following: 
        0. Log Out
        1. Deposit Account
        2. Withdraw Account
        3. Change Address
        4. Accounts Overview and Total
        5. Open New Account
        6. Close Account
        7. Close All Acounts and Delete Data
        8. Get transactions
        9. Visualize account
        """

        user_input = input(input_str)
        
        while user_input not in options.keys():
            user_input = input(input_str)
        return options[user_input]

    def loggedin_actions(self, action, customer):
        """
        carries out the action options taken by the user onto the customer object that is passed to it.
        """
        if action == "log_out":
            return
        elif action == "deposit":
            # Get amount to deposit / withdraw
            deposit_amount = input("Enter deposit amount")
            while not deposit_amount.isdigit():
                # in this case, negatives are not allowed since it would fail in isdigit()
                deposit_amount = input("Enter deposit amount")
            
            # Get the accounts available for deposit / withdrawals
            # this part COULD be abstracted out into a separate function
            account_indexes = [str(i) for i in range(len(customer.accounts))]
            account_options = "Please select from the following accounts to deposit:"
            for index in account_indexes:
                account_options = account_options + f"\n{index}. {customer.accounts[int(index)]}"
            
            # receive and verify input is in format / within options
            print(account_options)
            account_choice = input(">> ")
            while account_choice not in account_indexes:
                print(account_options)
                account_choice = input(">> ")
            
            customer.deposit_account(customer.accounts[int(account_choice)], int(deposit_amount))
            
        
        elif action == "withdraw":
            # Get amount to deposit / withdraw
            withdraw_amount = input("Enter withdrawal amount")
            while not withdraw_amount.isdigit():
                # in this case, negatives are not allowed since it would fail in isdigit()
                withdraw_amount = input("Enter withdrawal amount")
            
            # Get the accounts available for deposit / withdrawals
            account_indexes = [str(i) for i in range(len(customer.accounts))]
            account_options = "Please select from the following accounts to withdrawal:"
            for index in account_indexes:
                account_options = account_options + f"\n{index}. {customer.accounts[int(index)]}"
            
            # receive and verify input is in format / within options
            print(account_options)
            account_choice = input(">> ")
            while account_choice not in account_indexes:
                print(account_options)
                account_choice = input(">> ")
            
            customer.withdraw_account(customer.accounts[int(index)], int(withdraw_amount))
        

        elif action == 'visualize_account':
            # Get the accounts available for visualization
            account_indexes = [str(i) for i in range(len(customer.accounts))]
            account_options = "Please select from the following accounts to deposit:"
            for index in account_indexes:
                account_options = account_options + f"\n{index}. {customer.accounts[int(index)]}"
            
            # receive and verify input is in format / within options
            print(account_options)
            account_choice = input(">> ")
            while account_choice not in account_indexes:
                print(account_options)
                account_choice = input(">> ")
            
            account_chosen = customer.accounts[int(index)]
            
            customer.visualize_account(account_chosen)
        




        elif action == "open_new_acc":
            customer.create_account()
        

        elif action == "close_acc":
            self.bank.close_account(customer)

        elif action == "close_customer":
            customer_closed = self.bank.close_customer(customer)
            if customer_closed:
                return "closed_customer"
            else:
                pass

        elif action == "overview":
            customer.display_accounts()
        
        elif action == "change_address":
            customer.change_address()
        
        elif action == "get_transactions":
            # choices
            all_choices = ['all', 'ALL']
            account_indexes = [str(i) for i in range(len(customer.accounts))]
            account_options = "Please select from the following accounts to select, or type \"all\" to see transactions from all accounts"
            for index in account_indexes:
                account_options = account_options + f"\n{index}. {customer.accounts[int(index)]}"
            
            # receive and verify input is in format / within options
            print(account_options)
            account_choice = input(">> ")
            while account_choice not in all_choices + account_indexes:
                print(account_options)
                account_choice = input(">> ")            
            
            if account_choice in all_choices:
                customer.get_transactions_history()
            else:
                customer.get_transactions_history(customer.accounts[int(index)])

        
        
        
        




    def logging(self):
        """
        # define logging per each transaction with timestamp, and details of transaction
        """
        pass


    


    
    












#################################################################################
################################  TESTING  ######################################
#################################################################################


# # testing bank creation
# bank = Bank("BOA")
# print(bank.name)
# bank.create_customer()
# bank.create_account("18238591")



user_interface = UI("BOA")
# user_interface.begin()
user_interface.begin()

