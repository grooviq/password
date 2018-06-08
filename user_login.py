class User:
    """
    Class that generates new users login system
    """
    def __init__(self,fullname, email, username, password):
        
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password
    
    user_list = []


    def save_user(self):
        """
        method that saves user object to user_list
        """
        User.user_list.append(self)


    @classmethod
    def user_exists(cls, username):
        """
        Method that checks user existense in the user list.
        Args:
        username: user to search if the username exists
        Returns Boolean: True or false accordingly
        """
        for user in cls.user_list:
            if user.username == username:
                return True
            else:
                return False



    @classmethod
    def find_by_username(cls,username):
        
        for user in cls.user_list:
            if user.username == username:
                return user
            else:
                return 0