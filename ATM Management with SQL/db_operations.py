import sqlite3
from datetime import datetime

db_name = 'atm.db'


def create_db():
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()

    sql_command = """CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    fname VARCHAR(20),
    lname VARCHAR(30),
    pin VARCHAR(4),
    gender CHAR(1),
    balance INTEGER);"""

    cursor.execute(sql_command)
    sqliteConnection.close()


def delete_db():
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()

    cursor.execute("DROP TABLE users")
    sqliteConnection.close()


def read_users_table():
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT * FROM users")
    ans = cursor.fetchall()
    for i in ans:
        print("Acc. no", i[0], "firstname", i[1], "lastname", i[2], "pin", i[3], "gender", i[4], "balance_in_db", i[5])
    sqliteConnection.close()


def last_user_id():
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    ans = cursor.fetchall()
    return ans[0]


def get_user_by_id(user_id):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id={}".format(user_id))
    ans = cursor.fetchall()
    sqliteConnection.close()
    return ans


def add_entry_to_users(id, fname, lname, pin, gender, balance):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()

    present_date = datetime.now()
    command = "INSERT INTO users VALUES ({id}, '{fname}', '{lname}', '{pin}', '{gender}', {balance})".format(
        id=id, fname=fname, lname=lname, pin=pin, gender=gender, balance=balance
    )
    cursor.execute(command)
    sqliteConnection.commit()
    sqliteConnection.close()


def change_pin_by_id(user_id, newpin):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    command = "UPDATE users SET pin='{npin}' WHERE user_id={id}".format(npin=newpin, id=user_id)
    cursor.execute(command)
    sqliteConnection.commit()
    sqliteConnection.close()


def check_pin_by_id(user_id, pin_entered):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    command = "SELECT pin FROM users WHERE user_id={id}".format(id=user_id)
    cursor.execute(command)
    pin_in_db = cursor.fetchall()
    if pin_in_db[0][0] == pin_entered:
        return True
    return False


def check_balance_by_id(user_id):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    command = "SELECT balance FROM users WHERE user_id={id}".format(id=user_id)
    cursor.execute(command)
    balance_in_db = cursor.fetchall()
    return balance_in_db[0][0]


def update_balance_by_id(user_id, balance):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    command = "UPDATE users SET balance={nbalance} WHERE user_id={id}".format(nbalance=balance, id=user_id)
    cursor.execute(command)
    sqliteConnection.commit()
    sqliteConnection.close()

def get_all_user_ids():
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT user_id FROM users")
    user_ids = cursor.fetchall()
    sqliteConnection.close()
    return [user_id[0] for user_id in user_ids]

def delete_user_by_id(user_id):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    command = "DELETE FROM users WHERE user_id = ?"
    cursor.execute(command, (user_id,))
    sqliteConnection.commit()
    sqliteConnection.close()
read_users_table()
