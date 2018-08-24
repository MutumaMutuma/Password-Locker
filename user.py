# import unittest
class User :

    user_list = []
    def __init__ (self, account, username, password):
        self.account = account
        self.username = username
        self.password = password
        
    def save_user(self):
        User.user_list.append(self)

