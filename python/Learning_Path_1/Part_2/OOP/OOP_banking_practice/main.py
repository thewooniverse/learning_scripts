import random
from datetime import datetime

class Customer:
    def __init__(self, name, address, customer_id):
        self.name = name
        self.address = address
        self.customer_id = customer_id
        self.accounts = []
    
    def update_address(self, new_address):
        print(f"New address updated from {self.address} to {new_address}!")
        self.address = new_address
    
    def display_profile(self):
        print(f"Client Name: {self.name}\nClient Address: {self.address}")
    


class Account:
    def __init__(self, customer, account_number=str(random.randint(1, 10000000)), balance=0):
        self.account_number = account_number
        self.balance = balance
        self.customer = customer

        customer.accounts.append(self)
    
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
    def __init__(self):
        self.customers = []
        self.accounts = []
    
    def add_customer(self, customer):
        print(f"Adding customer {customer.name}...")
        self.customers.append(customer)

        # add all of the customer's existing accounts to the bank accounts
        for account in customer.accounts:
            if account not in self.accounts:
                print(f"Adding existing account {account.account_number} to accounts!")
                self.accounts.append(account)
        
    
    def remove_customer(self, customer):
        try:
            self.customers.remove(customer)
        except:
            print(f"This customer {customer.name} does not exist")
    
    def create_account(self, customer):
        # create and add new account
        new_account = Account(customer)
        self.accounts.append(new_account)
    
    def remove_account(self, account):
        try:
            self.accounts.remove(account)
        except:
            print(f"This account {account.account_number} does not exist")

    
    def get_total_deposits(self):
        return sum([account.balance for account in self.accounts])



# Test 1: Can we create a customer?
customer1 = Customer("Alice", "123 Cherry Lane", "CID152945")
assert customer1.name == "Alice"
assert customer1.address == "123 Cherry Lane"
# customer1.display_profile()
# customer1.update_address("Newfoundland 1592")
# assert customer1.address == "123 Cherry Lane" # prints assertion error
# customer1.display_profile()


# Test 2: Can we create an account?
account1 = Account(customer1)
assert account1.balance == 0
print(account1)
print(account1.account_number)
print(customer1.accounts)


# Test 3: Can we deposit and withdraw money?
account1.deposit(100)
assert account1.balance == 100
account1.withdraw(50)
assert account1.balance == 50

# Test 4: Can we create a bank and add customers and accounts?
bank = Bank()
bank.add_customer(customer1)
assert customer1 in bank.customers

bank.create_account(customer1)
print(bank.accounts)
assert account1 in bank.accounts

# Test 5: Do the bank's total deposits match the sum of its accounts?
assert bank.get_total_deposits() == 50

# Test 6: Can we update a customer's address?
customer1.update_address("456 Oak Street")
assert customer1.address == "456 Oak Street"

# Test 7: Can we remove an account?
bank.remove_account(account1)
assert account1 not in bank.accounts

# Test 8: Can we remove a customer?
bank.remove_customer(customer1)
assert customer1 not in bank.customers




