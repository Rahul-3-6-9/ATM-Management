import getpass
import string
import os

import db_operations

print("========================================")
print("........................................")
print("       WELCOME TO THE ATM SYSTEM        ")
print("........................................")
print("========================================")


while True:
    entry_Choice = int(input("If You Want To Register A User: Press 1 \nIf You Are Already Registered: Press 2 \n"))
    if entry_Choice==1:
        id = db_operations.last_user_id()[0] + 1
        print(":::::::::::::::::::::::::")
        first_name = input("ENTER YOUR FIRST NAME : ")
        last_name = input("ENTER YOUR LAST NAME : ")

        print("ENTER YOUR PIN (4 DIGITS) : ", end="")
        while True:
            pin = int(input())
            if (pin>=1000 and pin<=9999):
                break
            else:
                print("Wrong Format ... Please Enter Again", end="")

        print("ENTER YOUR GENDER(M - MALE /F - FEMALE /O - OTHERS /N - NOT WILLING TO MENTION) : ", end="")
        while True:
            gender = input()
            if (gender.upper() in ['M', 'F', 'O', 'N']):
                break
            else:
                print("Invalid Choice ... Please Enter Again", end="")

        print("ENTER YOUR DEPOSIT(LIMIT = 0) : ", end="")
        while True:
            deposit = int(input())
            if (deposit>0):
                break
            else:
                print("Below Limit ... Please Enter Again", end="")

        print("User Added Successfully")
        print(":::::::::::::::::::::::::\n\n")
        db_operations.add_entry_to_users(id, first_name, last_name, pin, gender, deposit)



    elif entry_Choice == 2:
        firstname = input("Enter your first name : ")
        firstname = firstname.lower()
        lastname = input("Enter your last name : ")
        lastname = lastname.lower()
        matching_list = db_operations.get_record(firstname, lastname)

        if len(matching_list) == 0:
            print("---------------------")
            print("   INVALID USERNAME  ")
            print("---------------------")
            break;

        print(":::::::::::::::::::::::::")
        pin = input("ENTER YOUR PIN : ")
        print(":::::::::::::::::::::::::")

        if db_operations.check_pin(firstname, lastname, pin) == False:
            print(":::::::::::::::::::::::::")
            print("PIN ENTERED IS INVALID")
            print(":::::::::::::::::::::::::")
            break;

        print("*************************")
        print("     LOGIN SUCCESSFUL    ")
        print("*************************")
        print(str.capitalize(firstname), " Welcome to MyBank ATM")

        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            response = input(
                "Select an option from the following that you would like to proceed with : Check Balance(c), Deposit(D), Withdraw(w), Change pin(p), Quit(q) : ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            # valid_responses = ['c', 'w', 'p', 'q', 'd']
            response = response.lower()

            if response == 'c':
                balance_user = db_operations.check_balance(firstname, lastname)
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("You have ", balance_user, " rupees in your account ")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif response == 'w':
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                withdraw = int(input("Enter the amount you would like to withdraw : "))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                balance_user = db_operations.check_balance(firstname, lastname)

                if withdraw > balance_user:
                    print("Insufficient balance : ")
                else:
                    balance_user = balance_user - withdraw
                    db_operations.update_balance(firstname, lastname, balance_user)
                    print("The amount you have withdrawn is : ", withdraw)
                    print("The amount left in your account is : ", balance_user)

            elif response == 'd':
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                deposit = int(input("Enter the amount you would like to deposit : "))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if deposit > 50000:
                    print("Deposit Limit Exceeded ...")
                else:
                    balance_user = db_operations.check_balance(firstname, lastname)
                    balance_user = balance_user + deposit
                    db_operations.update_balance(firstname, lastname, balance_user)
                    print("The amount you have deposit is : ", deposit)
                    print("The amount left in your account is : ", balance_user)

            elif response == 'p':
                print("________________________________________________")
                old_pin = input("Please enter your old pin : ")
                print("________________________________________________")

                if old_pin == pin:
                    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    new_pin = str(input("Please enter the new pin (4 digits): "))
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

                    if len(new_pin) == 4:
                        print("+++++++++++++++++++++++++++++++++")
                        pin_confirm = str(input("Confirm your new pin : "))
                        print("+++++++++++++++++++++++++++++++++")
                        if pin_confirm != new_pin:
                            print("PIN MISMATCH ! ")
                        else:
                            db_operations.change_pin(firstname, lastname, new_pin)
                            print("New pin saved")
                    else:
                        print("Your pin must contain 4 digits and must be different from your original pin")

                else:
                    print("Your pin is incorrect")

            elif response == 'q':
                print("Thank you for choosing MyBank")
                exit()

            else:
                print("!!!!!!!!!!!!!!!!!!!!")
                print("Response is not valid")


    else:
        print("!!!!!!!!!!!!!!!!!!!!")
        print("Response is not valid")