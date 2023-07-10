**Project Idea: A Simple Banking System**

Implement a simple banking system that consists of `Bank`, `Account`, and `Customer` classes.

1. **Customer Class:** A `Customer` class to represent a customer with attributes like `name`, `address`, and a unique `customer_id`. Methods might include `update_address()`, `display_profile()`, etc.

2. **Account Class:** An `Account` class that has attributes like `account_number` (unique to each Account object), `balance`. It should have methods like `deposit(amount)`, `withdraw(amount)`, and `check_balance()`. Each `Account` object is associated with one `Customer` object. 

3. **Bank Class:** Finally, a `Bank` class that contains multiple `Account` objects and `Customer` objects. It might have methods like `create_account(customer_id)`, `remove_account(account_number)`, `add_customer(customer)`, `remove_customer(customer_id)`, and `get_total_deposits()` (sum of all account balances).

You can play around with the code, add more functionalities, or make it more complex as per your understanding. 

This project will help you understand the practical implementation of OOP concepts like classes, objects, association, and aggregation. Have fun coding!

===
**TESTS**

Sure, here are some simple tests that you could use to verify the functionality of your banking system:

```python
# Test 1: Can we create a customer?
customer1 = Customer("Alice", "123 Cherry Lane")
assert customer1.name == "Alice"
assert customer1.address == "123 Cherry Lane"

# Test 2: Can we create an account?
account1 = Account(customer1)
assert account1.balance == 0

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
```

These tests check the main functionalities of your classes and their methods. You might need to adapt the code to fit the names of your classes and methods. Also, remember to import the necessary modules and classes at the beginning of your script.

Testing is a crucial part of the development process. It ensures that your code works as expected and helps you identify and fix bugs. Happy coding!




========================================================
Extension practice project ideas.
PIN number to display stuff and permissions
password + encryption logics
check balance

