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
