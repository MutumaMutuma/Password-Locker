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
# class Credential:
# 	'''
# 	Class to create  account credentials, generate passwords and save their information
# 	'''
# 	# Class Variables
# 	credentials_list =[]
# 	user_credentials_list = []
# 	@classmethod
# 	def check_user(cls,first_name,password):
# 		'''
# 		Method that checks if the name and password entered match entries in the users_list
# 		'''
# 		current_user = ''
# 		for user in User.user_list:
# 			if (user.first_name == first_name and user.password == password):
# 				current_user = user.first_name
# 		return current_user

# 	def __init__(self,user_name,media_page,account_name,password):
# 		'''
# 		Method to define the properties for each user object will hold.
# 		'''

# 		# instance variables
# 		self.user_name = user_name
# 		self.media_page = media_page
# 		self.account_name = account_name
# 		self.password = password

# 	def save_credentials(self):
# 		'''
# 		Function to save a newly created user instance
# 		'''
# 		# global users_list
# 		Credential.credentials_list.append(self)
# 	string = ''
# 	def generate_password(self, size=10, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
# 		'''
# 		Function to generate an 8 character password for a credential
# 		'''
# 		gen_pass=''.join(random.choice(char) for _ in range(size))
# 		return gen_pass

# 	@classmethod
# 	def display_credentials(cls,user_name):
# 		'''
# 		Class method to display the list of credentials saved
# 		'''
# 		user_credentials_list = []
# 		for credential in cls.credentials_list:
# 			if credential.user_name == user_name:
# 				user_credentials_list.append(credential)
# 		return user_credentials_list
				

	
# 	@classmethod
# 	def find_by_site_name(cls, media_page):
# 		'''
# 		Method that takes in a media_page and returns a credential that matches that media_page.
# 		'''
# 		for credential in cls.credentials_list:
# 			if credential.media_page == media_page:
# 				return credential