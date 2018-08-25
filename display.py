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
#To delete a user
def del_contact(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
#------------------------------------------------------------
def main():
    print("\033[1;36;1m PASSWORD LOCKER App\n")
    print("________________________________________________________")
    prom = input("Hello, welcome to Password Locker there whats your name: ")
    print("Aloha, " + prom + ", To get you started up kindly choose one of the following \n CN -> To Create an Account \n Log -> To log in \n ex -> Exit")



if __name__ == '__main__':
	main()