from abc import abstractmethod, ABC
# include an enum type
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Bank:

    def __init__(self,name):
        self.name = name
        self.__customers = []

    @property
    def num_customers(self):
        return len(self.__customers)
    
    @property
    def num_accounts(self):
        return sum([len(customer.__accounts) for customer in self.__customers])
    
    @property
    def total_bank_balance(self):
        return sum([customer.total_balance for customer in self.__customers])

    def add_customer(self, customer):
        logger.info(f"Registering {customer.name} to our bank")
        self.__customers.append(customer)
        return customer

    def remove_customer(self, customer_idx):
        """
        naive implementation. next best is to remove upon lookup
        of customer name
        """
        self.__customers.pop(customer_idx)

class Customer:

    def __init__(self,name):
        self.name = name 
        self.__accounts = []

    @property
    def total_balance(self):
        return sum([account.balance for account in self.__accounts])

    def open_account(self, account):
        logger.info(f"Opening account '{account.name}' for {self.name}")
        self.__accounts.append(account)
        return account

    def close_account(self, account_idx):
        self.__accounts.pop(account_idx)

    def list_accounts(self):
        for account in self.__accounts:
            logger.info(account)

    def get_account(self, account_idx):
        return self.__accounts[account_idx]
    

class Account:

    def __init__(self, name):
        self.name = name 
        # add a type, consider whether to refactor into abstract class after
        # on call vs savings vs term deposit, for eg
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    def __str__(self):
        return f"Account(name={self.name}, balance={self.balance})"

    def __repr__(self):
        return f"Account(name={self.name}, balance={self.balance})"

    def deposit(self, amount): # abstractify this, because some accounts only allow deposits up to certain amount
        self.__balance += amount
        logger.info(f"Deposited ${amount}. Current balance: {self.balance}")

    def withdraw(self, amount): # abstractify this, because some accounts allow overdraft
        if self.__balance - amount < 0:
            logger.error(f"Insufficient funds to withdraw ${amount}")
        else:
            logger.info(f"Withdrawn ${amount}. Current balance: {self.balance}")
        return amount

    def transfer(self, amount, other):
        self.__balance -= amount
        other.balance += amount

    def get_balance(self):
        logger.info(f"Current account balance: {self.balance}")

def main():

    bank = Bank("online")
    nicole = bank.add_customer(Customer("Nicole"))
    nic_savings = nicole.open_account(Account("Savings"))
    nicole.list_accounts()
    nic_savings.deposit(300)
    nic_savings.withdraw(400)
    nic_savings.get_balance()
    logger.info(nicole.total_balance) # change to getter instead?
    logger.info(bank.total_bank_balance) # change to getter instead?


if __name__ == '__main__':
    main()

    





    





    