# ATM Management System

A simple ATM Management System built using **Python** and **SQLite**. This project simulates basic ATM functionalities such as account creation, deposits, withdrawals, balance inquiries, and transaction history management.

## Features

- **Account Creation**: Register new customer accounts.
- **Deposits**: Add funds to existing accounts.
- **Withdrawals**: Withdraw funds, ensuring sufficient balance.
- **Balance Inquiry**: Check current account balance.
- **Changing Pin**: Allows user to change the pin.
- **Account Deletion**: Allows the user to delete their account if needed.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Rahul-3-6-9/ATM-Management.git
   cd ATM-Management

2. **Initialize the Database**

    Open db_operations.py.

    Run the script:

    ```bash
    python db_operations.py

3. **Run the Main Program**

    ```bash
    python main.py
    
## Technologies Used

1. Python 3: Core programming language.

2. SQLite: Lightweight relational database for storing account and transaction data.

## Note

1. Ensure that db_operations.py is executed before running main.py to set up the necessary database tables.

2. All data is stored locally in the database.db file.
