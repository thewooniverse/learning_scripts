OVERALL LESSONS:
Its better to make each class do thigns simply.
In my case, it is better to allow for the UI class to handle all the UI / inputting functions, and keep things simple on the bank level.







To do's:

3. Customer closure
4. Multi bank transfers of accounts

>>>> Troubleshoot the deposit bug where it deposits to only one account
5. sum methods to display amounts!

(bug) - close account feature is not functioning correctly for single account users;
4. Changing details of customers
5. Getpass / password access and controlled access

7. Forgot password feature + change PIN (pw) feature -> it would be cool to eventually authenticate this somehow;
-> asks user if they forgot password
-> A code is randomly generated and sent to user (currently it is printed, later it will be sent to an email or phone number using Twilio)
-> If the user inputs the number correctly, they are then able to change their PIN.

--- completed above---


1. Txn history
--> create a new dataframe
---> transaction logs? or tables
customer level -> overview of all accounts and all accounts transaction history, for eacha ccount held by customer bring in the dataframe and combine it; loop thru.
-------------

1.5 Visualization of accounts and customer;
- total bar line graph of all account balances over time;
visualization on the account level and on the customer level (same stuff being done on different levels)
- spend by month / spend by day, inflow outflow by the day
- balance over time


2. Encryption of TX history / csvs

3. Twilio integration for enabling 2FA


4. Multi bank .transfer() functionality

5. Debugs / error logs / unit tests and refactoring for maintenance
- Unit tests
- Docstrings
- pdb / debugging

6. pay() functionality


7. Ability to search for transactions










-- Docstrings and tidy up.

Core functionality / features:
- Users can access and unencrypt their accounts using their PIN
- Users can create, remove and change their customer details
- Users can create new accounts, close accounts and withdraw or deposit from their accounts
- Users can access all these features using a clean User Interface
- The application logs all transaction details into a CSV file
