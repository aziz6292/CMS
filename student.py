# BCSF19A026
# Abdul Aziz
from user import User
class Student(User):
    def __init__(self, username="New User", password="default123", sem=1, cgpa=0.0, degree='BCS'):
        super().__init__(username, password)
        if isinstance(sem, int) and sem > 0 and sem <= 8:
            self.__semester = sem
        else:
            self.__semester = 1
        if isinstance(cgpa, (float, int)) and cgpa >= 0 and cgpa <= 4:
            self.__CGPA = cgpa
        else:
            self.__CGPA = 0.0
        if degree in (['BCS', 'BSE', 'BIT', 'BDS']):
            self.__degree = degree
        else:
            self.__degree = 'BCS'
    @property
    def semester(self):
        return self.__semester
    @semester.setter
    def semester(self, sem):
        if isinstance(sem, int) and sem > 0 and sem <= 8:
            self.__semester = sem
        else:
            raise ValueError("Invalid Range of Semester")
    @property 
    def cgpa(self):
        return self.__CGPA
    @cgpa.setter
    def cgpa(self, cgpa):
        if isinstance(cgpa, (float, int)) and cgpa >= 0 and cgpa <= 4:
            self.__CGPA = cgpa
        else:
            self.__CGPA = 0.0
    @property
    def degree(self):
        return self.__degree
    @degree.setter
    def degree(self, degree):
        if degree in (['BCS', 'BSE', 'BIT', 'BDS']):
            self.__degree = degree
        else:
            self.__degree = 'BCS'
