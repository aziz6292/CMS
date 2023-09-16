# BCSF19A026
# Abdul Aziz

class Course:
    def __init__(self, c_id, c_name):
        if isinstance(c_id, int):
            self.__course_id = c_id
        else: raise ValueError ('Invalid Course ID')
        self.__course_name = c_name
    @property 
    def course_id(self):
        return self.__course_id
    @property
    def course_name(self):
        return self.__course_name
    @course_id.setter
    def course_id(self, c_id):
        if isinstance(c_id, int):
            self.__course_id = c_id
        else:
            raise ValueError('course id is invalid must be int')
    @course_name.setter
    def course_name(self, c_name):
        self.__course_name = c_name


