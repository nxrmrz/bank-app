"""
A file for storing classes representing bank entities
"""

import datetime
import logging
from typing import List, Dict, Union

from . import utils

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Account:
    """
    Class for instantiating a bank account
    """
    def __init__(self, account_number: str):
        self.__account_number = account_number
        self.__balance: float = 0.0
        self.__transactions: List[Transaction] = []

    @property
    def account_number(self) -> str:
        """
        Getter method to return the immutable account number
        """
        return self.__account_number

    @property
    def balance(self) -> Union[float, int]:
        """
        Getter method to return the account's (mutable) balance
        """
        return self.__balance
    
    @balance.setter
    def balance(self, value: Union[float,int]):
        """
        Setter method to set the account's (mutable) balance
        """
        utils.validate_amount(value)
        self.__balance = value
    
    def deposit(self, amount: float):
        """
        Deposits an amount of money to the account
        """
        utils.validate_amount(amount)
        self.balance += amount
        self._add_transaction("deposit", amount)

    def withdraw(self, amount: float):
        """
        Withdraws an amount of money from the account and checks if withdrawal is possible
        """
        utils.validate_amount(amount)
        if amount <= self.balance:
            self.balance -= amount
            self._add_transaction("withdrawal", amount)
        else:
            logger.error(f"Insufficient funds in account '{self.account_number}' for withdrawing ${amount}")

    def _add_transaction(self, transaction_type: str, amount: float):
        """
        Encapsulates a transaction type and amount against the account 
        types include deposits, withdrawals, and future scenarios like transfers
        """
        utils.validate_amount(amount)
        assert(isinstance(transaction_type,str))
        transaction = Transaction(self, transaction_type, amount)
        self.__transactions.append(transaction)

class Customer:
    """
    Class for instantiating a bank customer
    """
    def __init__(self, name: str):
        self.name = name
        self.__accounts: Dict[str, Account] = {}

    @property
    def accounts(self) -> Dict[str, Account]:
        """
        Getter method for accessing customer accounts (mutable)
        """
        return self.__accounts
    
    @accounts.setter
    def accounts(self, value: Dict):
        """
        Setter method for setting customer accounts (mutable)
        """
        assert(isinstance(value, Dict))
        self.__accounts = value

    def add_account(self, account: Account):
        """
        Adds a bank account to a customer
        """
        assert(isinstance(account, Account))
        self.accounts[account.account_number] = account

    def get_account(self, account_num: str) -> Account:
        """
        Returns a bank account given the account number
        """
        assert(isinstance(account_num, str))
        return self.accounts[account_num]
    
    def _calculate_balance(self) -> float:
        """
        Calculates the total account balance across a customer's accounts
        """
        return sum(account.balance for _, account in self.__accounts.items())

    def display_total_balance(self):
        """
        Displays the total account balance with a message
        """
        logger.info(f"{self.name}'s total balance: ${self._calculate_balance()}")

class Transaction:
    """
    Class for instantiating a transaction against a bank account
    Transactions can include deposits, withdrawals, and future ones like transfers
    """
    def __init__(self, account: Account, transaction_type: str, amount: float, timestamp: datetime.datetime =None):
        self.__account = account
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__timestamp = timestamp if timestamp else datetime.datetime.now()
        logger.info(self)
    
    def __str__(self) -> str:
        """
        Sets the string representation of a transaction object
        """
        return f"{self.__transaction_type} on {self.__account.account_number} of ${self.__amount}"