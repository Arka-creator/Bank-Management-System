🏦 Bank Management System

A simple Bank Management System built using Python and Object-Oriented Programming (OOP) concepts.

This is a menu-driven console application that allows users to create and manage different types of bank accounts.

📌 Features
Create a Bank Account
Create a Savings Account
Create a Current Account
Deposit money
Withdraw money
Check account balance
Add interest to Savings Accounts
Support overdraft for Current Accounts
Display all account details
Prevent duplicate account numbers
Handle invalid account number input
Exit the program safely
🛠️ Technologies Used
Python
Object-Oriented Programming (OOP)
📚 OOP Concepts Used


1. Classes and Objects

The project uses different classes to represent different types of bank accounts.

BankAccount
SavingsAccount
CurrentAccount

Objects are created from these classes and stored in a list.


2. Inheritance

SavingsAccount and CurrentAccount inherit from the BankAccount class.

class SavingsAccount(BankAccount):
class CurrentAccount(BankAccount):

This allows the child classes to reuse the properties and methods of the parent class.


3. Encapsulation

The account balance is declared as a private variable.

self.__balance = balance

The balance is accessed using:

get_balance()

And modified using:

set_balance()
4\. Method Overriding

The CurrentAccount class overrides the withdraw() method from the BankAccount class.

This allows a Current Account to withdraw money using its available balance and overdraft limit.


5. Polymorphism

Different types of account objects are stored in the same list.

accounts = \[\]

The same methods, such as withdraw() and display_account_info(), can behave differently depending on the object type.


6. Exception Handling

The project uses try and except to handle invalid account number input.

try:
account_number = int(input("Enter account number: "))
except ValueError:
print("Account number must be an integer.")
7\. isinstance()

The isinstance() function checks whether an account is a SavingsAccount before adding interest.

if isinstance(account, SavingsAccount):
account.add_interest()
🏦 Account Types
Bank Account

A basic bank account that supports:

Deposit
Withdrawal
Balance checking
Displaying account information
Savings Account

A Savings Account inherits from BankAccount and provides:

Interest calculation
Adding interest to the account balance
Current Account

A Current Account inherits from BankAccount and provides:

Overdraft facility
Custom withdrawal functionality
📋 Menu Options
===== BANK MANAGEMENT SYSTEM =====


1. Create Bank Account
2. Create Savings Account
3. Create Current Account
4. Deposit Money
5. Withdraw Money
6. Check Balance
7. Add Interest
8. Display All Accounts
9. Exit


