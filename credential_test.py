import unittest
from credential import credential
import pyperclip

class credential_test(unittest.TestCase):
	'''
	test class that defines test cases for the credential class
	'''
    def setUp(self):
    	'''
    	set up method to run each test case
    	'''
    	self.new_cred = Credential ("facebook","grooviq","grooviqdeejay@gmail.com","254groove")

    def test_init(self):
    	'''
    	test init to test the object initialization
    	'''
    	self.assertEqual(self.new_cred.accountName, "facebook")
    	self.assertEqual(self.new_cred.username, "Grooviq")
    	self.assertEqual(self.new_cred.email, "grooviqdeejay@gmail.com")
    	self.assertEqual(self.new_cred.password, "254groove")

    def tearDown(self):
    	'''
    	tear down metthod that cleans up after running each testcase
    	'''
    	Credential.cred_list = []
