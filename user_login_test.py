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