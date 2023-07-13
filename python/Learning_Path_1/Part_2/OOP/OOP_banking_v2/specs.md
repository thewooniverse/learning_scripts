**Customers**
- Customers have a name, address, customer_id, PIN and accounts they are holding with the given bank
- Customers can hold multiple account objects
- Customers can update their addresses
- Customers can display the accounts held with a specific bank
-- Customers can only be created by and contained inside specific bank databases
-- A customer may have separate accounts with multiple banks, or multiple accounts with the same bank.

**Accounts**
- Accounts have balance, belongs_to, bank_held, account_number and eventually each account is password protected
- Accounts can deposit or withdraw balances

**Banks**
- Banks hold multiple customer information

- Banks can add (onboard) or remove customers
- Banks can add or remove accounts from customers
- Banks can authenticate customers before accessing customer information or other permissions
- Banks can interact with users to perform actions on their accounts

**File Structures**
- [bank_name]_customers.json: holds persistent data through different sessions
- main.py: carries most of the script




**Other notes**
Eventually, this will need a separate database to hold the public / private keys for encryption decryption as well as PINs and saving accounts.

SQLite? Json? Pickle?
I'll probably write Pickle, JSON is not a good way to use this for now.
Pickle, and graduate it in the future with SQLite maybe.

Do I store objects here? Or store them in JSON.
Each has their pros and cons.


**Development Roadmap**

