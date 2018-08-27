import unittest
import random
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Argumentss:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Instagram", "Suwa", "12345") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.account,"Instagram")
        self.assertEqual(self.new_user.username,"Suwa")
        self.assertEqual(self.new_user.password,"12345")
    def test_save_multiple_user(self):
            '''
            test_save_multiple_contact to check if we can save multiple user
            objects to our contact_list ueegfu
            '''
            self.new_user.save_user()
            test_user = User("Instagram", "Suwa", "12345") # new user
            test_user.save_user()
            # test_user.save_contact()
            self.assertEqual(len(User.user_list),2)    
# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)            

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Instagram", "Suwa", "12345")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)
        #---------------------------------------------------------------------------------
    def test_find_user_by_account(self):

        self.new_user.save_user()
        test_user = User("Instagram", "Suwa", "12345")
        test_user.save_user()

        found_user = User.find_by_account("Instagram")

        self.assertEqual(found_user.username, test_user.username)
    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("Instagram", "Suwa", "12345")
        test_user.save_user()

        user_exists = User.user_exist("Instagram")

        self.assertTrue(user_exists)
    def test_display_all_users(self):
        self.assertEqual(User.display_users(), User.user_list)