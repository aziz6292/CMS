# BCSF19A026
# Abdul Aziz
class User:
    def __init__(self, username = "New User", password = "default123"):
        self.__username = username
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, value):
        if value is not None:
            self.__username = value
        else: raise ValueError("Invalid username")
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        if value is not None:
            self.__password = value
        else: raise ValueError("Invalid password")
