class BankAccount:
    def __init__(self, name, account_number, account_type, balance):
        """Constructor to initialize the bank account details."""
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        """Method to deposit an amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """Method to withdraw an amount from the account after checking the balance."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient balance for the withdrawal.")
        else:
            print("Withdrawal amount must be greater than zero.")

    def display_details(self):
        """Method to display the details of the bank account."""
        print(f"\nAccount Details:")
        print(f"Name of Depositor: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")

# Function to get user input and create a bank account
def create_account():
    name = input("Enter the name of the depositor: ")
    account_number = input("Enter the account number: ")
    account_type = input("Enter the account type (e.g., Savings, Checking): ")
    initial_balance = float(input("Enter the initial balance: "))

    # Create a new BankAccount object
    account = BankAccount(name, account_number, account_type, initial_balance)

    # Display the details of the account
    account.display_details()

    return account

# Function to interact with the account
def manage_account(account):
    while True:
        print("\nChoose an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Display Account Details")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display_details()
        elif choice == '4':
            print("Exiting the account management.")
            break
        else:
            print("Invalid choice. Please try again.")

# Main program to create an account and manage it
if __name__ == "__main__":
    account = create_account()
    manage_account(account)

