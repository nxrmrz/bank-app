"""
A file for testing bank entities
"""

import unittest
import unittest.mock

from src.bank_entities import Customer, Account, Transaction

class TestCustomer(unittest.TestCase):

    def setUp(self):
        # mock single customer and account
        self.customer = Customer("Alice")
        self.account = Account("123456")

        #mock single customer, multiple accounts
        self.customer_multiple = Customer('John')
        self.customer_multiple.accounts = {
            'customer1': Account("78910"),
            'customer2': Account("11123")
        }
        for _, accounts in self.customer_multiple.accounts.items():
            accounts.balance = 150
        
        
    def test_add_account(self):
        self.customer.add_account(self.account)
        self.assertIn("123456", self.customer.accounts)

    def test_get_account(self):
        self.customer.add_account(self.account)
        retrieved_account = self.customer.get_account("123456")
        self.assertEqual(retrieved_account, self.account)

    def test__calculate_balance(self):
        self.assertEqual(self.customer_multiple._calculate_balance(), 300)

    def test_display_total_balance(self):
        # mock logger
        with unittest.mock.patch('logging.Logger.info') as mock_info:
            self.customer_multiple.display_total_balance()
            mock_info.assert_called_once_with("John's total balance: $300")

class TestAccount(unittest.TestCase):

    def setUp(self):
        # mock single account
        self.account = Account("123456")

    def test_deposit_int(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 100)

    def test_deposit_float(self):
        self.account.deposit(100.0)
        self.assertEqual(self.account.balance, 100.0)

    def test_withdraw_sufficient_funds(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def test_withdraw_insufficient_funds(self):
        self.account.deposit(50)
        with self.assertLogs() as cm:
            self.account.withdraw(100)
        self.assertTrue(any("Insufficient funds" in msg for msg in cm.output))

class TestTransaction(unittest.TestCase):
    def test_transaction_str(self):
        account = Account("123456")
        transaction = Transaction(account, "deposit", 100)
        expected_str = "deposit on 123456 of $100"
        self.assertEqual(str(transaction), expected_str)