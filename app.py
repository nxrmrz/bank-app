from src.bank import Bank
from src.bank_entities import Customer, Account

def main():

    # instantiate a bank
    bank = Bank()

    # creating customers and accounts for them
    for idx, customer in enumerate([Customer("Alice"), Customer("Bob")]):
        bank.add_customer(customer)
        account_number = f"acc_{idx}" #simulating generation of unique account numbers
        customer.add_account(Account(account_number))

    alice = bank.get_customer("Alice") #getting via name for this demo, get via customer ID in production

    # integration test scenario on Alice
    alice_acc = alice.get_account("acc_0")
    alice_acc.deposit(30.0) #accepts float
    alice_acc.withdraw(20) #accepts int too
    alice.display_total_balance()
    bank.display_total_balance()

    bob = bank.get_customer("Bob")
    bob_acc = bob.get_account("acc_1")
    bob_acc.deposit(50)
    bank.display_total_balance()

    alice_acc.withdraw(11) # should fail

if __name__ == '__main__':
    main()