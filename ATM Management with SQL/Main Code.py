import getpass
import string
import os
import db_operations


print("========================================")
print("........................................")
print("       WELCOME TO THE ATM SYSTEM        ")
print("........................................")
print("========================================")

wrong_input = 0
while True:
    entry_Choice = input("If You Want To Register A User: Press 1 \nIf You Are Already Registered: Press 2 \nIf You Want to Delete an Account: Press 3 \n")
    if entry_Choice == '1':
        print(":::::::::::::::::::::::::")
        id = int(input("ENTER YOUR ACCOUNT NUMBER: "))
        while (id in db_operations.get_all_user_ids()):
            print("!!!ENTER THE CORRECT ACCOUNT NUMBER!!!")
            id = int(input("ENTER YOUR ACCOUNT NUMBER: "))

        first_name = input("ENTER YOUR FIRST NAME : ").lower()
        last_name = input("ENTER YOUR LAST NAME : ").lower()

        print("ENTER YOUR PIN (4 DIGITS) : ", end="")
        while True:
            pin = int(input())
            if pin >= 1000 and pin <= 9999:
                break
            else:
                print("Wrong Format ... Please Enter Again", end="")

        print("ENTER YOUR GENDER(M - MALE /F - FEMALE /O - OTHERS /N - NOT WILLING TO MENTION) : ", end="")
        while True:
            gender = input().upper()
            if gender in ['M', 'F', 'O', 'N']:
                break
            else:
                print("Invalid Choice ... Please Enter Again", end="")

        print("ENTER YOUR DEPOSIT(LIMIT = 0) : ", end="")
        while True:
            deposit = int(input())
            if deposit > 0:
                break
            else:
                print("Below Limit ... Please Enter Again", end="")

        print("User Added Successfully")
        print(":::::::::::::::::::::::::\n\n2")
        db_operations.add_entry_to_users(id, first_name, last_name, pin, gender, deposit)

    elif entry_Choice == '2':
        user_id = input("Enter your Account Number: ")
        user_id = int(user_id)

        matching_list = db_operations.get_user_by_id(user_id)

        if len(matching_list) == 0:
            print("---------------------")
            print("   INVALID ACCOUNT   ")
            print("---------------------")
            break

        print(":::::::::::::::::::::::::")
        pin = input("ENTER YOUR PIN : ")
        print(":::::::::::::::::::::::::")

        if db_operations.check_pin_by_id(user_id, pin) == False:
            print(":::::::::::::::::::::::::")
            print("PIN ENTERED IS INVALID")
            print(":::::::::::::::::::::::::")
            break

        print("*************************")
        print("     LOGIN SUCCESSFUL    ")
        print("*************************")
        print("Welcome to MyBank ATM")

        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            response = input(
                "Select an option from the following that you would like to proceed with : Check Balance(c), Deposit(D), Withdraw(w), Change pin(p), Quit(q) : ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            response = response.lower()

            if response == 'c':
                balance_user = db_operations.check_balance_by_id(user_id)
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("You have ", balance_user, " rupees in your account ")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif response == 'w':
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                withdraw = int(input("Enter the amount you would like to withdraw : "))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                balance_user = db_operations.check_balance_by_id(user_id)
                if response.lower() == 'return':
                    continue
                if withdraw > balance_user:
                    print("Insufficient balance : ")
                else:
                    balance_user = balance_user - withdraw
                    db_operations.update_balance_by_id(user_id, balance_user)
                    print("The amount you have withdrawn is : ", withdraw)
                    print("The amount left in your account is : ", balance_user)

            elif response == 'd':
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                deposit = int(input("Enter the amount you would like to deposit : "))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if response.lower() == 'return':
                    continue
                if deposit > 50000:
                    print("Deposit Limit Exceeded ...")
                else:
                    balance_user = db_operations.check_balance_by_id(user_id)
                    balance_user = balance_user + deposit
                    db_operations.update_balance_by_id(user_id, balance_user)
                    print("The amount you have deposited is : ", deposit)
                    print("The amount left in your account is : ", balance_user)

            elif response == 'p':
                print("________________________________________________")
                old_pin = input("Please enter your old pin : ")
                print("________________________________________________")
                if response.lower() == 'return':
                    continue

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
                            db_operations.change_pin_by_id(user_id, new_pin)
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

    elif entry_Choice == '3':
        print(":::::::::::::::::::::::::")
        id = int(input("ENTER YOUR ACCOUNT NUMBER: "))
        while (id not in db_operations.get_all_user_ids()):
            print("!!!ENTER THE CORRECT ACCOUNT NUMBER!!!")
            id = int(input("ENTER YOUR ACCOUNT NUMBER: "))

        print(":::::::::::::::::::::::::")
        pin = input("ENTER YOUR PIN : ")
        print(":::::::::::::::::::::::::")

        if db_operations.check_pin_by_id(id, pin) == False:
            print(":::::::::::::::::::::::::")
            print("PIN ENTERED IS INVALID")
            print(":::::::::::::::::::::::::")
            break

        print("PLEASE CONFIRM THE DELETION OF THE ACCOUNT BY TYPING \"CONFIRM\"")
        confirmation=input().lower()
        if (confirmation=="confirm"):
            db_operations.delete_user_by_id(id)

    else:
        if wrong_input == 2:
            print("!!!!!!!!!!!!!!!!!!!!")
            print("You have failed 3 times .... Closing Session")
            break

        wrong_input += 1
        print("!!!!!!!!!!!!!!!!!!!!")
        print("Response is not valid ... Tries left: ", 3 - wrong_input)
