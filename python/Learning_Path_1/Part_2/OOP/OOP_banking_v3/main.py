#! python3
# pylint: disable=pointless-string-statement


# import modules
from getpass import getpass
import os
import pickle

"""
To do's:


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

        # randomly generate a customer ID and create the customer path
        customer_id = "18238591"
        customer_path = f"{self.customers_path}{os.path.sep}{customer_id}.pkl"


        # create the object
        new_customer = Customer(customer_name, customer_address, customer_id, customer_pin, customer_path)

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
        with open(f"{self.customers_path}{os.path.sep}{target_customer_id}.pkl", 'rb') as f:
            # randomly generate account_ID for customer
            customer_object = pickle.load(f)
            new_account_id = "18581295921"

            # create a new account and add it to the customer object's account
            new_account = Account(new_account_id)
            customer_object.accounts.append(new_account_id)

            # save the account object in the accounts directory
            with open(self.accounts_path + f'{os.path.sep}{new_account_id}.pkl', 'wb') as f:
                pickle.dump(new_account, f)
        
            # save the target customer object (reconcile)
            with open(customer_object.path, 'wb') as old_file:
                pickle.dump(customer_object, old_file) #dump the currently open customer object into the old file




class Customer:
    """
    Customer objects are accessed by the user, through the banking UI.
    They are stored as pickle files and their methods / functions can only be accessed if the PIN they entered is correct
    Eventually, all of their files will be encrypted and in order to unlock them, you would need to enter the correct PIN

    >> To Do's
    > get total account sum / accounts overview

    """

    def __init__(self, name, address, cid, pin, path):
        self.name = name
        self.address = address
        self.accounts = [] # accounts is a list that stores account_IDs associated with this customer, at init it is empty
        self.cid = cid

        # PIN should be an encrypted result so that the raw object saved does not contain the actual PIN but an encrypted version
        self.pin = pin
        self.path = path
    
    
    # check / refresh account details after saving / transaction

    # create new account

    # account_deposit (account, amount)

    # account_withdraw (account, amount)

    # access account


class Account:
    def __init__(self, account_id):
        # does not contain information on who owns the accounts

        self.balance = 0
        self.account_id = account_id



# # testing bank creation
bank = Bank("BOA")
# print(bank.name)
# bank.create_customer()
bank.create_account("18238591")


# testing customer file persistence
with open(f'{os.getcwd()}{os.path.sep}BOA{os.path.sep}customers{os.path.sep}18238591.pkl', 'rb') as f:
    customer = pickle.load(f)
    print(customer)
    print(customer.name)
    print(customer.pin)
    print(customer.cid)
    print(customer.accounts)




