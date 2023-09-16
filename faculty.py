# BCSF19A026
# Abdul Aziz
from user import User
class Faculty(User):
    def __init__(self, username="New User", password="default123", desg = 'Professor', subject = 'BCS'):
        super().__init__(username, password)
        self.__Designation = desg
        self.__subject = subject
    @property 
    def designation(self):
        return self.__Designation
    @property
    def subject(self):
        return self.__subject
    @designation.setter
    def designation(self, des):
        self.__Designation = des
    @subject.setter
    def subject(self, sub):
        self.__subject = sub