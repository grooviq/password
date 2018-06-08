import random

class Credential:
    """
    class that generates new prompt requirements of user credentials
    """
    def __init__(self, accountName, email, username, password):
        self.accountName = accountName
        self.email = email
        self.username = username
        self.password = password
    
    cred_list = []
