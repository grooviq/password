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

    def test_save_cred(self):
    	"""
        test_save_cred test case to test if the cred object is saved to
         cred list
        """
        self.new_cred.save_cred()
        self.assertEqual(len(Credential.cred_list), 1)

    def test_cred_exists(self):
        """
        test_profile_exist to check if there is another matching or similar profile
        """
        self.new_cred.save_cred()
        test_cred = Credential("facebook", "grooviqdeejay@gmail.com","grooviq","254groove")    
        test_cred.save_cred()
        cred_exists = Credential.cred_exists("facebook")
        self.assertTrue(cred_exists)

    def test_find_cred_by_accountName(self):
        """
        test to check if we can find user credentials by accountName
        """
        self.new_cred.save_cred()
        test_cred = Credential("facebook", "grooviqdeejay@gmail.com","grooviq","254groove")
        test_cred.save_cred()
        found_cred = Credential.find_by_accountName("facebook")
        self.assertEqual(found_cred.accountName,test_cred.accountName)

    def test_display_all_credentials(self):
        """
        test to check display all user accounts s
        """
        self.assertEqual(Credential.display_accounts(), Credential.cred_list)

    def test_delete_credentials(self):
        """
        test_delete_profile to test deletion of user profile
        """
        self.new_cred.save_cred()
        test_cred = Credential("facebook", "grooviqdeejay@gmail.com","grooviq","254groove")
        test_cred.save_cred()
        self.new_cred.delete_cred()
        self.assertEqual(len(Credential.cred_list), 1)

