#!/usr/bin/env python3.6
import pyperclip
from user import User
#To add an account
def create_contact(account,username,password):
    '''
    Function to create a new account
    '''
    new_user = User(account,username,password)
    return new_user
#To save a user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
def find_user(account):
    return User.find_by_account(account)
def check_existing_user(account):
    return User.user_exist(account)
def display_users():
    return User.display_users()
#------------------------------------------------------------
def main():
    print("\033[1;36;40m PASSWORD LOCKER App\n")
    print("")
    prom = input("Hello, welcome to Password Locker there whats your name: ")
    print("  ")
    print("Aloha, " + prom + ", To get you started up kindly choose one of the following")
    print(" ")
    print("\033[1;34;1m  Options On how to Get Started on Password Locker\n")
    print("")
    # print("\033[1;35;1m cc -> To Create an Account\n")
    # print("\033[1;35;1m Log -> To log in\n")
    # print("\033[1;35;1m ex -> Exit\n")
    while True:
        print("Use these short codes : \n cc - create an account\n dc - display username\nfc -find a user\nex -exit the user list ")
        print(" ")
        short_code = input('Enter : ').lower().strip()
        if short_code == 'cc':
            print('To create a new account: ')
            first_name = input("Enter the first name: ")
            last_name = input("Enter your last name: ")
            password = input("Enter your password: ")
            print("\033[1;32;1m  \n")
            print( first_name +" "+ last_name + " You have successfully signed in to Password Locker using password " + password)
            print("-------------- ")
            print("To save an account, Enter the respective credentials :  ")
            print("--------------ssss")
            account = input("Enter the name of the account that you want to store:  ")
            username = input("Enter the username you are using:  ")
            password = input("Enter your password:  ")
            save_user(User(account, username, password ))
            print("\033[1;31;1m You have successfully saved your Credentials \n")
            # print(emoji.emojize('Python is :thumbs_up_sign:'))
            print("\033[1;32;1m  \n")
        elif short_code == "dc":
            if display_users():
                print("Here is a list of all your Accounts")
                print("\n")
                # for user in display_users():
                user = User.display_user()
                print("\033[1;37;1m  \n")
                print(f"Site: {user.account} \n User Name: {user.username} \n Password: {user.password}")
                    # print(user)
            else:
                print("\033[1;32;1m  \n")
                print(" ")
                print("You don't seem to have any accounts created yet")       
if __name__ == '__main__':
	main()