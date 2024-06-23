# Python code for ATM interface

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw: ${amount}")
        else:
            print("Insufficient funds.")

    def transfer(self, to_account, amount):
        if amount <= self.balance:
            self.withdraw(amount)
            to_account.deposit(amount)
            self.transaction_history.append(f"Transfer: ${amount} to {to_account.name}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Available balance: ${self.balance}")

    def display_transaction_history(self):
        for i, transaction in enumerate(self.transaction_history, start=1):
            print(f"{i}. {transaction}")


if __name__ == "__main__":
    account1 = BankAccount("User 1")
    account2 = BankAccount("User 2")

    while True:
        print("\nATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction history")
        print("6. Exit")

        option = int(input("Enter your option: "))

        if option == 1:
            account1.check_balance()
        elif option == 2:
            amount = float(input("Enter the deposit amount: "))
            account1.deposit(amount)
        elif option == 3:
            amount = float(input("Enter the withdrawal amount: "))
            account1.withdraw(amount)
        elif option == 4:
            amount = float(input("Enter the transfer amount: "))
            account2.transfer(account1, amount)
        elif option == 5:
            account1.display_transaction_history()
        elif option == 6:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")










