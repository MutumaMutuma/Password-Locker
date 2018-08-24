import unittest
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
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
            test_user =User("Instagram", "Suwa", "12345") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)    


if __name__ == '__main__':
    unittest.main()