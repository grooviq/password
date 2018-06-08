import unittest
from user_login import User

class user_test(unittest.TestCase):
    """
    Test class that defines test cases for the user_login class behaviours
    
    """

    def setUp(self):
        """
        set up method to run each test case
        """
        self.new_user = User("victor maina","grooviqdeejay@gmail.com","grooviq","254groove")

    def test_init(self):
        """
        test init test case to test proper object initialization
        """

        self.assertEqual(self.new_user.fullname,"victor maina")
        self.assertEqual(self.new_user.email,"grooviqdeejay@gmail.com")
        self.assertEqual(self.new_user.username, "grooviq")
        self.assertEqual(self.new_user.password, "254groove")

    def test_create_new_account(self):
        """
        test_create_new_account test case to test if the new user is
        saved to user list
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        """
        teardown method that does 'clean up' after each test case has run
        """
        User.user_list = []


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        """
        test_check_user_exists to test if a user exists or not
        """
        self.new_user.save_user()
        test_user = User("victor maina","grooviqdeejay@gmail.com","grooviq","254groove")
        test_user.save_user()
        user_exists = User.user_exists("grooviq")
        self.assertTrue(user_exists)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User()
        test_user.save_user()
        found_user = User.find_by_username("grooviq")
        self.assertEqual(found_user.password,test_user.password

if __name__ == '__main__':
    unittest.main()



