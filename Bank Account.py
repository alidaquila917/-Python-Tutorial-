import os

class BankAccount:
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountID = self.generate_account_id()
        self.statement_file = f"{self.name}_{self.accountType}_{self.accountID}.txt"
        self.create_statement_file()

    def generate_account_id(self):
        # Simulate generating a unique account ID
        return hash((self.name, self.accountType))

    def create_statement_file(self):
        # Create a new statement file for the account
        with open(self.statement_file, "w") as file:
            file.write("Transaction History:\n")

    def deposit(self, amount):
        self.balance += amount
        with open(self.statement_file, "a") as file:
            file.write(f"Deposited: ${amount}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            with open(self.statement_file, "a") as file:
                file.write(f"Withdrew: ${amount}\n")

    def get_balance(self):
        return self.balance

    def get_user_id(self):
        return self.accountID

    def get_username(self):
        return self.name

    def get_account_type(self):
        return self.accountType

    def get_transaction_history(self):
        with open(self.statement_file, "r") as file:
            return file.read()

# Test the BankAccount class
account1 = BankAccount("John", "savings")
account2 = BankAccount("Alice", "chequing", 500)

# Perform transactions
account1.deposit(1000)
account1.withdraw(200)
account2.deposit(200)
account2.withdraw(100)

# Display account information and transaction history
print("Account 1 Balance:", account1.get_balance())
print("Account 1 ID:", account1.get_user_id())
print("Account 1 Username:", account1.get_username())
print("Account 1 Type:", account1.get_account_type())
print("Account 1 Transaction History:")
print(account1.get_transaction_history())

print("\nAccount 2 Balance:", account2.get_balance())
print("Account 2 ID:", account2.get_user_id())
print("Account 2 Username:", account2.get_username())
print("Account 2 Type:", account2.get_account_type())
print("Account 2 Transaction History:")
print(account2.get_transaction_history())
