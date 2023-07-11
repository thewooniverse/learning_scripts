import random
from datetime import datetime

class Customer:
    def __init__(self, name, address, customer_id):
        self.name = name
        self.address = address
        self.customer_id = customer_id
    
    def update_address(self, new_address):
        print(f"New address updated from {self.address} to {new_address}!")
        self.address = new_address
    
    def display_profile(self):
        print(f"Client Name: {self.name}\nClient Address: {self.address}")
    

class Account:
    def __init__(self, account_number, customer_id, balance=None):
        self.account_number = account_number
        self.balance = balance
        self.customer_id = customer_id
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}\nNew account balance: {self.balance}')
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f'Withdrew {amount}\nNew account balance: {self.balance}')
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")
        return(self.balance)

class Bank:
    def __init__(self, customers, accounts):
        self.customers = customers
        self.accounts = accounts
    
    def add_customer(self, name, address):
        # randomly generate a Customer ID that is not already in use
        random_num = random.randint(1, 100000)
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime('%Y%m%d')
        new_customer_id = f"CID-{formatted_date}-{random_num}"
        assert new_customer_id not in [customer.customer_id for customer in self.customers]
        # this should be optimized in the future with sorting algorithms potentially
        # and this would spur me to try out testing / runtimes and begin learning on optimizations!

        new_customer = Customer(name, address, new_customer_id)
        print("New customer created")
        new_customer.display_profile()
        self.customers.append(new_customer)
    

    def remove_customer(self, rm_customer_id):
        # try to find
        for customer in self.customers:
            if customer.customer_id == rm_customer_id:
                self.customers.remove(customer)
                print(f"Removed customer: {rm_customer_id}")
                return
        
        # if it loops through without finding it, we print not found message and return
        print(f"Customer: {rm_customer_id} does not exist in the system")
        return
    
    def create_account(self, customer):
        # randomly generate a Account ID that is not already in use
        random_num = random.randint(1, 100000)
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime('%Y%m%d')
        new_account_id = f"AID-{formatted_date}-{random_num}"
        assert new_account_id not in [account.account_id for account in self.accounts]

        # create and add the new account into accounts
        new_account = Account(new_account_id, customer.customer_id)
        self.accounts.append(new_account)
    
    def remove_account()






# Test 1: Can we create a customer?
customer1 = Customer("Alice", "123 Cherry Lane", "CID152945")
assert customer1.name == "Alice"
assert customer1.address == "123 Cherry Lane"
# customer1.display_profile()
customer1.update_address("Newfoundland 1592")
# assert customer1.address == "123 Cherry Lane" # prints assertion error
# customer1.display_profile()







