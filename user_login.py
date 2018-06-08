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