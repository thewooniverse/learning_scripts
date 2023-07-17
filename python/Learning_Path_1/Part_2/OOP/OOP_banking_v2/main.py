# import modules
from getpass import getpass
import os
import pickle


# define customer class
class Customer():
    def __init__(self, name, address, customer_id, pin):
        self.name = name
        self.address = address
        self.customer_id = customer_id
        self.pin = pin

        # by default it is initially set to [], but this value MIGHT change if I need to use something else than a list
        self.accounts = []
        self.accounts_path = f'{os.getcwd()}/{customer_id}.pkl'

        # if it doesn't exist create the file first
        if not os.path.exists(self.accounts_path):
            with open(self.accounts_path, 'wb') as f:
                pickle.dump(self.accounts, f)

        # then load the file as self.accounts
        with open(self.accounts_path, 'rb') as f:
            self.accounts = pickle.load(f)
        
    def authenticate(self):
        password_provided = getpass("Please enter your PIN: ")
        return password_provided == self.pin
        # eventually this needs to "unlock" encrypted data -> need to determine what is encrypted, what isn't.

    def update_address(self, new_address):
        self.address = new_address
        print(f"Address updated to {new_address}")

    

# Customer class unit tests
# abby = Customer("Abby Lane","baby lane 19241", "BOA_49135_129", "1234")
# pickle is to store the customer's accounts and account details

