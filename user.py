# import unittest
class User :

    user_list = []
    def __init__ (self, account, username, password):
        self.account = account
        self.username = username
        self.password = password

    contact_list = [] # Empty contact list
 # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
    def delete_user(self):
        User.user_list.remove(self)
    @classmethod
    def find_by_account(cls, account):
        for user in cls.user_list:
            if user.account == account:
                return user
    @classmethod
    def user_exist(cls, account):
        for user in cls.user_list:
            if user.account == account:
                return True
        
        return False
    @classmethod
    def display_users(cls):
        return cls.user_list

    @classmethod
    def display_user(cls):
        for user in cls.user_list:
            return user