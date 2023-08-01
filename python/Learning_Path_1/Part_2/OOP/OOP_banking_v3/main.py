#! python3

# import modules
from getpass import getpass
import os
import pickle

#SPECS: In the future, 
## - Forgot password?





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
        >> check for duplicates so that data does not get corrupted
        """

        print("Please enter your name\n")
        customer_name = input(">> ")

        print("Please enter your address\n")
        customer_address = input(">> ")

        print("Please enter your four digit PIN\n")
        customer_pin = input(">> ")

        # randomly generate a customer ID from
        customer_id = "18238591"

        # create the object
        new_customer = Customer(customer_name, customer_address, customer_id, customer_pin)

        # save the object in self.path
        with open(self.customers_path + f'{os.path.sep}{customer_id}.pkl', 'wb') as f:
            pickle.dump(new_customer, f)
    
    # delete existing customer

    # change customer information

    # authenticate customer / access information
    ## user_id / account_id then ask for PIN

    

    ## account related methods ##
    def create_account(self, customer):

        # randomly generate account_d
        new_account_id = "1858129"

        # create a new account and add it to the customer accounts
        new_account = Account(new_account_id)
        customer.accounts.append(new_account_id)



class Customer:
    """
    Customer objects are accessed by the user, through the banking UI.
    They are stored as pickle files and their methods / functions can only be accessed if the PIN they entered is correct
    Eventually, all of their files will be encrypted and in order to unlock them, you would need to enter the correct PIN

    >> To Do's
    > get total account sum / accounts overview

    """


    def __init__(self, name, address, cid, pin):
        self.name = name
        self.address = address
        self.accounts = [] # accounts is a list that stores account_IDs associated with this customer, at init it is empty
        self.cid = cid

        # PIN should be an encrypted result so that the raw object saved does not contain the actual PIN but an encrypted version
        self.pin = pin
        
    # check / refresh account details after saving / transaction

    # create new account


    # account_deposit (account, amount)

    # account_withdraw (account, amount)

    # access account


class Account:
    def __init__(self, account_id):
        self.balance = 0
        self.account_id = account_id
    
    



# # testing bank creation
# bank = Bank("BOA")
# print(bank.name)
# bank.create_customer()

# testing customer file persistence
with open(f'{os.getcwd()}{os.path.sep}BOA{os.path.sep}customers{os.path.sep}18238591.pkl', 'rb') as f:
    customer = pickle.load(f)
    print(customer.name)
    print(customer.pin)
    print(customer.cid)
