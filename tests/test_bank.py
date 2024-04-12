"""
A file for testing the bank
"""

import unittest
from unittest.mock import MagicMock

from src.bank import Bank
from src.bank_entities import Customer

class TestBank(unittest.TestCase):
    
    def setUp(self):
        #mock bank setup for single customer
        self.bank = Bank()

        #mock bank setup for multiple customers
        self.bank_multiple = Bank()
        self.bank_multiple.customers = {
            'customer1': MagicMock(spec=Customer),
            'customer2': MagicMock(spec=Customer)
        }
        for _, customer in self.bank_multiple.customers.items():
            customer._calculate_balance.return_value = 150

    def test_add_customer(self):
        customer = Customer("Alice")
        self.bank.add_customer(customer)
        self.assertIn("Alice", self.bank.customers)

    def test_get_customer(self):
        customer = Customer("Bob")
        self.bank.add_customer(customer)
        retrieved_customer = self.bank.get_customer("Bob")
        self.assertEqual(retrieved_customer, customer)

    def test__calculate_balance(self):
        self.assertEqual(self.bank_multiple._calculate_balance(), 300)

    def test_display_total_balance(self):
        #mock logger
        with unittest.mock.patch('logging.Logger.info') as mock_info:
            self.bank_multiple.display_total_balance()
            mock_info.assert_called_once_with("Bank's total balance: $300")