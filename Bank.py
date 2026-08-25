class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid withdrawal amount.")
    def set_balance(self,amount):
        self.__balance = amount
    def get_balance(self):
        return self.__balance
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.get_balance()}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() +self.overdraft_limit:
            balance = self.get_balance()
            balance -= amount
            self.set_balance(balance)
            print(f"Withdrew {amount}. New balance is {self.get_balance()}.")
        else:
            print("Invalid withdrawal amount.")

accounts = []

running = True
while (running):
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Bank Account")
    print("2. Create Savings Account")
    print("3. Create Current Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Check Balance")
    print("7. Add Interest")
    print("8. Display All Accounts")
    print("9. Exit")

    choice = input("Enter your choice: ")
    match choice:
        case "1":
            try:
                account_number = int(input("Enter account number: "))
            except ValueError:
                print("Account number must be an integer.")
                continue
            if (account_number in [account.account_number for account in accounts]):
                print("Account number already exists. Please choose a different account number.")
                continue
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            account = BankAccount(account_number, account_holder, initial_balance)
            accounts.append(account)
            print("Bank account created successfully.")
        case "2":
            try:
                account_number = int(input("Enter account number: "))
            except ValueError:
                print("Account number must be an integer.")
                continue
            if (account_number in [account.account_number for account in accounts]):
                print("Account number already exists. Please choose a different account number.")
                continue
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            interest_rate = float(input("Enter interest rate (as a decimal): "))
            account = SavingsAccount(account_number, account_holder, initial_balance, interest_rate)
            accounts.append(account)
            print("Savings account created successfully.")
        case "3":
            try:
                account_number = int(input("Enter account number: "))
            except ValueError:
                print("Account number must be an integer.")
                continue
            if (account_number in [account.account_number for account in accounts]):
                print("Account number already exists. Please choose a different account number.")
                continue
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            overdraft_limit = float(input("Enter overdraft limit: "))
            account = CurrentAccount(account_number, account_holder, initial_balance, overdraft_limit)
            accounts.append(account)
            print("Current account created successfully.")
        case "4":
            try:
                account_number = int(input("Enter account number: "))
            except ValueError:
                print("Account number must be an integer.")
                continue
            amount = float(input("Enter amount to deposit: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.deposit(amount)
                    break
            else:
                print("Account not found.")
        case "5":
            try:
                account_number = int(input("Enter account number: "))
            except ValueError:
                print("Account number must be an integer.")
                continue
            amount = float(input("Enter amount to withdraw: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.withdraw(amount)
                    break
            else:
                print("Account not found.")
        case "6":
            try:
                account_number = int(input("Enter account number: "))
            except ValueError:
                print("Account number must be an integer.")
                continue
            for account in accounts:
                if account.account_number == account_number:
                    print(f"Balance: {account.get_balance()}")
                    break
            else:
                print("Account not found.")
        case "7":
            try:
                account_number = int(input("Enter account number: "))
            except ValueError:
                print("Account number must be an integer.")
                continue
            for account in accounts:
                if isinstance(account, SavingsAccount) and account.account_number == account_number:
                    account.add_interest()
                    break
            else:
                print("Savings account not found.")
        case "8":
            for account in accounts:
                account.display_account_info()
        case "9":
            print("Exiting the program.")
            running = False
        case _:
            print("Invalid choice. Please try again.")