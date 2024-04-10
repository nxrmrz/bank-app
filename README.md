# TODO:
- assertions
- type hinting
- error handling

# ways to improve
- code each transaction against an account as an object, so we could store history

# Class Diagrams

Decide classes and methods per class
then decide static vs class vs instance attributes
then decide public/private/protected
then decide getters/setters
then run through SOLID principles for refactoring
Leetcode 2x a day

Bank
- has many customers
- stores all customer accounts

- Properties:
- name (public, class var)
- num customers (private, class var)
- total balance across all customers (private, class var)

- Methods:
- register_customer()

b=Bank()
b.open_account(Nicole, 'oncall') #once registered
b.close_account(nicole)

nicole.list_accounts() #list of account names
nicole.check_balance() #returns a balance
nicole.deposit(money, acc)
nicole.withdraw(money, acc)
nicole.transfer(money, acc1, acc2)

Customer
- has many accounts
- deposit()
- withdraw()
- check() #checks balance
- transfer() - OPTIONAL - transfers balance across accounts
- has name, ID, total balance across accounts

Account
- can be multiple for each customer
- container for customer money
- has name, number (the ID of the class), balance property

# Tests to write

● Deposit, withdraw and maintain a balance for multiple customers
● Return a customer’s balance and the bank’s total balance
● Prevent customers from withdrawing more money than they have in their account
An example test scenario
When Alice deposits $30 and withdraws $20
Then Alice’s balance will be $10 and the bank’s balance will be $10
And Alice will be prevented from withdrawing $11 to prevent her balance going negative