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

# Credential Class functions
def create_cred(accountName, email, username, password):
    """
    Function to create new credentials
    """
    new_cred = User(accountName, email, username, password)
    return new_cred

def save_new_cred(new_cred):
    """
    Function to save credentials
    """
    new_cred.save_cred()

def del_cred(cred):
    """
    Function to delete credentials
    """
    cred.delete_cred()

def check_existing_cred(accountName):
    """
    Function that check if credentials exist with exact accountName
    """
    return Credential.cred_exists(accountName)

def find_cred(accountName):
    """
    Function that finds a user's credentials by accountName and returns the credentials
    """
    return Credential.find_by_accountName(accountName)

def gen_password(username):

    return Credential.gen_password(username)

def display_accounts():
    """
    Function that returns all the saved accounts
    """
    return Credential.display_accounts()

# main

def main():
    print("Welcome to Password Locker")
    print("-"*10)

    while True:
        print("Please use the following short codes:")
        print ("si - Sign-up, lo - Login, ex - Exit")
        print('\n')
        short_code = input().lower()

        if short_code == 'si':
            print("Sign up to create a Password Locker account")
            print("-"*20)

            print("Fullname.....")
            fullname = input()

            print("Email Address.....")
            email = input()

            print("Username.....")
            username = input()

            print("Password.....")
            password = input()

            save_new_user(User(fullname, email, username, password))
            print('\n')
            print(f"Welcome {username}, your account has successfully been created")
            print ('\n')

        elif short_code == 'lo':
            print("Login to your Password Locker account")
            print("-"*20)

            # while True:

            print("Username.....")
            search_user = input()
            if check_existing_user(search_user):
                user_find = find_user(search_user)
                # while True:
                print(" Input Password.....")
                password = input()
                if password == user_find.password:
                    print(f"Welcome {username}, you are logged in!")
                    print ('\n')