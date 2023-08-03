#! python3
# pylint: disable=pointless-string-statement


# import modules
from getpass import getpass
import os
import pickle

"""
Still to do - complete the UI class and methods to provide baseline user features:
- access account / login
- deposit, withdraw etc...

To do's:
1. Develop UI class and methods for interacting with bank objects ++ authenticating
2. Add RNG for account IDs and others
3. Removing customer and accounts
4. Changing details of customers and sum methods
5. Encryption and getpass / password access and controlled

6. Datetime of deposit logs / transaction logs
7. Graph plot of balances in and out / balances over time
** 8. Transferring balances between accounts **


-- Docstrings and tidy up.

Core functionality:
- Users can access and unencrypt their accounts using their PIN
- Users can create, remove and change their customer details
- Users can create new accounts, close accounts and withdraw or deposit from their accounts
- Users can access all these features using a clean User Interface
- The application logs all transaction details into a CSV file
"""

# create bank object
class Bank:
    def __init__(self, name):
        self.name = name

        # other data in the future can be saved in a pickle and picked up / saved to keep it persistent

        # check if there is already a directory with the name in current dir, if not create one and its sub directories
        self.path = f'{os.getcwd()}/{name}'
        self.customers_path = self.path + os.path.sep + "customers"
        self.accounts_path = self.path + os.path.sep + "accounts"

        if not os.path.exists(self.path):
            os.mkdir(self.path)
            os.mkdir(self.customers_path)
            os.mkdir(self.accounts_path)


    ## customer methods ##
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
        customer_id = "18238591"

        # create the object
        new_customer = Customer(customer_name, customer_address, customer_id, customer_pin, self.path)

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
            print("Invalid Credentials: Customer does not exist")
            return None # parent method will call this method again

        else:
            with open(f"{self.customers_path}{os.path.sep}{cid}.pkl", 'rb') as f:
                customer_object = pickle.load(f)
                
                # check credentials
                if (cid, pin) == (customer_object.cid, customer_object.pin):
                    print(f'Welcome {customer_object.name} you are now logged in.')
                    return customer_object
                print(customer_object.cid, customer_object.pin)
                return None



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
        self.accounts = [] # accounts is a list that stores account_IDs associated with this customer, at init it is empty
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
        new_account_id = "185812959"

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
        assert account_id in self.accounts
        
        # find and open the account
        with open(f'{self.accounts_path}{os.path.sep}{account_id}.pkl', 'rb') as f:
            account_object = pickle.load(f)
            # call the deposit function on the account
            account_object.deposit(amount)

    # account_withdraw (account, amount)
    def withdraw_account(self, account_id, amount):
        # check that the account is indeed owned by this customer
        assert account_id in self.accounts

        with open(f'{self.accounts_path}{os.path.sep}{account_id}.pkl', 'rb') as f:
            account_object = pickle.load(f)
            # call the deposit function on the account
            account_object.withdraw(amount)



    # access account


class Account:
    def __init__(self, account_id, bank_path):
        # does not contain information on who owns the accounts
        self.balance = 0
        self.account_id = account_id
        self.bank_path = bank_path
        self.path = f"{bank_path}{os.path.sep}accounts{os.path.sep}{account_id}.pkl"
    
    def reconcile(self):
        """
        account.reconcile()
        -- Description --
        opens self.path and dumps itself into the path.
        -- Usage --
        """
        with open(self.path, 'wb') as f:
            pickle.dump(self, f)


    def deposit(self, amount):
        self.balance += amount
        self.reconcile()
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal unavailable, amount exceeds current balance")
        else:
            self.balance -= amount
        self.reconcile()
        
    
    def check_balance(self):
        print(f'Current balance: ${self.balance}')
        return(self.balance)

    


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
                break
            elif response == "login":
                loggedin_customer = self.bank.authenticate()
                while not loggedin_customer:
                    loggedin_customer = self.bank.authenticate()
                    # loop / use logged in options to carry out actions.
                    # then you can also choose to log out.

            elif response == 'create_new_acc':
                self.bank.create_customer()
            
            elif response == "forgot_password":
                print("You forgot da password!")
    
    
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
            "0": "exit",
            "1": "login",
            "2": "create_new_acc",
            "3": "forgot_password"
        ""}
        input_str = f"""Please select from the following: 
        0. Deposit Account
        1. Withdraw Account
        2. Change Customer Information
        3. Get Total Accounts Balance
        4. Open New Account
        5. Close Account
        6. Close All Acounts and Delete Data
        # 7. Transfer
        """

        user_input = input(input_str)
        
        while user_input not in options.keys():
            user_input = input(input_str)
        return options[user_input]




    def logging(self):
        """
        # define logging per each transaction with timestamp, and details of transaction
        """
        pass


    


    
    












#################################### testing ####################################


# # testing bank creation
# bank = Bank("BOA")
# print(bank.name)
# bank.create_customer()
# bank.create_account("18238591")


# testing customer file persistence
# with open(f'{os.getcwd()}{os.path.sep}BOA{os.path.sep}customers{os.path.sep}18238591.pkl', 'rb') as f:
#     customer = pickle.load(f)
#     print(customer)
#     print(customer.name)
#     print(customer.pin)
#     print(customer.cid)
#     print(customer.accounts)

#     customer.withdraw_account('185812959', 1000)


# with open(f'{os.getcwd()}{os.path.sep}BOA{os.path.sep}accounts{os.path.sep}185812959.pkl', 'rb') as f:
#     account = pickle.load(f)
#     account.check_balance()

user_interface = UI("BOA")
# user_interface.begin()
user_interface.begin()

