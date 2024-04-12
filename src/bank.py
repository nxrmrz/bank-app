"""
A file for storing the Bank class
"""

import logging
from typing import Dict

from .bank_entities import Customer

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Bank:
    """
    A class for instantiating a bank
    """
    def __init__(self):
        self.__customers: Dict[str, Customer] = {}

    @property
    def customers(self) -> Dict[str, Customer]:
        """
        Getter method for accessing customers of bank (mutable)
        """
        return self.__customers

    @customers.setter
    def customers(self, value: Dict[str, Customer]):
        """
        Setter method for setting customers of bank (mutable)
        """
        assert(isinstance(value, Dict))
        self.__customers = value
    
    def add_customer(self, customer: Customer):
        """
        Adds a customer to the bank
        """
        assert(isinstance(customer, Customer))
        self.customers[customer.name] = customer

    def get_customer(self, customer_name: str) -> Customer:
        """
        Returns a customer given the customer name
        """
        assert(isinstance(customer_name, str))
        return self.customers[customer_name]
    
    def _calculate_balance(self) -> float:
        """
        Calculates the total balance of the bank across customers and their accounts
        """
        return sum([customer._calculate_balance() for _, customer in self.__customers.items()])

    def display_total_balance(self):
        """
        Displays the total balance of the bank across customers and their accounts with a message
        """
        logger.info(f"Bank's total balance: ${self._calculate_balance()}")