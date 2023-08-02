#! python3
# pylint: disable=pointless-string-statement


# import modules
from getpass import getpass
import os
import pickle

"""
To do's:
1. Develop UI methods
2. Add RNG for account IDs and others
3. Removing customer and accounts
4. Changing details of accounts
5. Encryption and getpass / password access and controlled

Docstrings and tidy up.
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

    # UI methods



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

    ## user_id / account_id then ask for PIN -> or perhaps the UI / terminal side shoudl be a separate object to interact with?
    # Logging in and logging out UI

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
        - opens self.path and dumps itself into the path.
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



