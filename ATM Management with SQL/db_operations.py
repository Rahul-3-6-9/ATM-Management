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
    # created_on DATETIME DEFAULT CURRENT_TIMESTAMP);"""

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
        print("S.no",i[0],"firstname",i[1],"lastname",i[2],"pin",i[3],"gender",i[4],"balance_in_db",i[5])
    sqliteConnection.close()

def last_user_id():
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    ans = cursor.fetchall()
    return ans[0]

def get_record(firstname, lastname):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT * FROM users where fname='{name1}' AND lname='{name2}'".format(name1=firstname,
                                                                                      name2=lastname))
    ans = cursor.fetchall()
    sqliteConnection.close()
    return ans

def add_entry_to_users(id, fname, lname, pin, gender, balance):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()

    # Get last user_id, add 1 to it and use that as the next user_id
    # cursor.execute("SELECT TOP 1 * FROM users")
    # ans = cursor.fetchall()
    # print(ans)

    present_date = datetime.now()
    command = "INSERT INTO users VALUES ({id}, '{fname}', '{lname}', '{pin}', '{gender}', {balance})".format(
        id=id, fname=fname, lname=lname, pin=pin, gender=gender, balance=balance
    )
    # print(command)
    cursor.execute(command)
    # cursor.execute("INSERT INTO users VALUES ({}, {}, {}, {}, {}, 0)".format(
    #     id, fname, lname, pin, gender, 0))
    sqliteConnection.commit()
    sqliteConnection.close()


def change_pin(fname, lname, newpin):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    command = "UPDATE users SET pin={npin} where fname='{fnametosearch}' AND lname='{lnametosearch}'".format(
        npin=newpin,
        fnametosearch=fname,
        lnametosearch=lname)
    cursor.execute(command)
    sqliteConnection.commit()
    sqliteConnection.close()


def check_pin(passed_fname, passed_lname, pin_entered):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    command = "SELECT pin from users where fname='{fname}' AND lname='{lname}'".format(fname=passed_fname,
                                                                                       lname=passed_lname)
    cursor.execute(command)
    pin_in_db = cursor.fetchall()
    # print (pin_in_db[0][0])
    if pin_in_db[0][0] == pin_entered:
        return True
    return False


def check_balance(passed_fname, passed_lname):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    command = "SELECT balance from users where fname='{fname}' AND lname='{lname}'".format(fname=passed_fname, lname=passed_lname)
    cursor.execute(command)
    balance_in_db = cursor.fetchall()
    print (balance_in_db[0][0])
    return balance_in_db[0][0]


def update_balance(fname, lname, balance):
    sqliteConnection = sqlite3.connect('atm.db')
    cursor = sqliteConnection.cursor()
    command = "UPDATE users SET balance={nbalance} where fname='{fnametosearch}' AND lname='{lnametosearch}'".format(
        nbalance=balance,
        fnametosearch=fname,
        lnametosearch=lname)
    cursor.execute(command)
    sqliteConnection.commit()
    sqliteConnection.close()


# delete_db()
# create_db()
#
# add_entry_to_users(1, 'rahul', 'suresh', 3434, 'M', 10000)
# add_entry_to_users(2, 'suriyaa', 'prasath', 9090, 'M', 20000)
# add_entry_to_users(3, 'rakesh', 'arumugam', 1234, 'M', 5000)
# add_entry_to_users(4, 'pranav', 'duvvuri', 4153, 'M', 14500)
# add_entry_to_users(5, 'mahesh', 'saravanan', 7767, 'M', 12000)
#
#
# value = check_pin('enid', 'blyton', '5678')
# print(value)
# check_balance('enid', 'blyton')
#
# read_users_table()
read_users_table()