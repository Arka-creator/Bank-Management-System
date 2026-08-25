# 🏦 Bank Management System

A simple Bank Management System built using Python and Object-Oriented Programming (OOP).

## Features

- Create Bank Account
- Create Savings Account
- Create Current Account
- Deposit Money
- Withdraw Money
- Check Balance
- Add Interest
- Display All Accounts

## Technologies Used

- Python
- Object-Oriented Programming (OOP)

## OOP Concepts Used

### Inheritance

`SavingsAccount` and `CurrentAccount` inherit from `BankAccount`.

### Encapsulation

The account balance is kept private using:

`self.__balance`

### Method Overriding

`CurrentAccount` overrides the `withdraw()` method to support overdraft functionality.

### Polymorphism

Different account objects are stored in the same `accounts` list and can use common methods.

## How to Run

Clone the repository:

```bash
git clone <(https://github.com/Arka-creator/Bank-Management-System/edit/main/README.md)>
python Bank.py
