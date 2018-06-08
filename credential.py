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

    def save_cred(self):
        """
        save_cred method saves user credentials into cred_list
        """
        Credential.cred_list.append(self)

    @classmethod
    def cred_exists(cls,accountName):        
        """
        method to check if profile exists
        
        Returns:
            Boolean: True or false accordingly
                   """
        
        for cred in cls.cred_list:
            if cred.accountName == accountName:
                return True
            else:
                return False 

    def delete_cred(self):
        """
        delete_profile method that deletes a specified profile
        """
        Credential.cred_list.remove(self)

    @classmethod
    def display_accounts(cls):
        """
        method that returns the cred list
        """
        return cls.cred_list

    @classmethod
    def find_by_accountName(cls,accountName):
        """
        Method that takes in an account name and returns matching credentials
        
        
        """

        for cred in cls.cred_list:
            if cred.accountName == accountName:
                return cred
