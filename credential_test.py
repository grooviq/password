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
    	self.new_cred = Credential ("facebook","grooviq","grooviqdeejay2gmail.com","password")

    