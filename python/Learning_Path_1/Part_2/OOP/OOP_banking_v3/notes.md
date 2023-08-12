
To do's:

3. Customer closure
4. Multi bank transfers of accounts

>>>> Troubleshoot the deposit bug where it deposits to only one account
5. sum methods to display amounts!

(bug) - close account feature is not functioning correctly for single account users;
4. Changing details of customers
5. Getpass / password access and controlled access

--- completed above---


7. Forgot password feature + change PIN (pw) feature -> it would be cool to eventually authenticate this somehow;
-> asks user if they forgot password
-> A code is randomly generated and sent to user (currently it is printed, later it will be sent to an email or phone number using Twilio)
-> If the user inputs the number correctly, they are then able to change their PIN.


8. Encryption





6. Datetime of deposit logs / transaction logs into bank's database
--> create a new dataframe
---> transaction logs? or tables
dataframe where...
exists on the customer level
- index is the datetime
- account that is deposited / withdrawn
- amount that is deposited / withdrawn
- amount that the account has before + after the deposit
- logs all accounts for a given customer


6.5. Visualization of accounts and customer;
- total bar line graph of all account balances over time;




9. debugging / error logging

Each of these last elements introduce a new module to be used: cryptography, datetime and pandas, matplotlib

--------

LEARN MATPLOT / Pandas related features
7. Graph plot of balances in and out / balances over time from transaction logs both on the user level, and on the bank level.
-- transaction histories and visualization
8. Full encryption features of transaction history and data
9. Transferring balances between accounts and reconciling

--------
I think this would be enough function / features for now.






-- Docstrings and tidy up.

Core functionality / features:
- Users can access and unencrypt their accounts using their PIN
- Users can create, remove and change their customer details
- Users can create new accounts, close accounts and withdraw or deposit from their accounts
- Users can access all these features using a clean User Interface
- The application logs all transaction details into a CSV file
