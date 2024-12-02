class BankAccount:
    def __init__(self, name, account_number, account_type, balance=0):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_details(self):
        print("\nAccount Details:")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")

# Taking inputs from the user
name = input("Enter account holder's name: ")
account_number = input("Enter account number: ")
account_type = input("Enter account type (e.g., Savings, Checking): ")
balance = float(input("Enter initial balance: "))

# Creating a BankAccount instance
account = BankAccount(name, account_number, account_type, balance)

# Display account details and interact with the account
while True:
    print("\nChoose an action:")
    print("1. Display account details")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        account.display_details()
    elif choice == "2":
        deposit_amount = float(input("Enter amount to deposit: "))
        account.deposit(deposit_amount)
    elif choice == "3":
        withdraw_amount = float(input("Enter amount to withdraw: "))
        account.withdraw(withdraw_amount)
    elif choice == "4":
        print("Thank you for using the bank account system!")
        break
    else:
        print("Invalid choice. Please try again.")

