from credential import credential
from user_login import User 

# User Class functions
def create_user(fullname, email, username, password):
    """
    Function to create a new user
    """
    new_user = User(fullname, email, username, password)
    return new_user

def save_new_user(new_user):
    """
    Function to save user
    """
    new_user.save_user()

def check_existing_user(username):
    """
    Function that check if a user exists & login details
    """
    return User.user_exists(username)

def find_user(username):
    """
    Function that finds a user by username
    """
    return User.find_by_username(username)