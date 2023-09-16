# BCSF19A026
# Abdul Aziz
from student import Student
from faculty import Faculty
from utility import Utility

class View:
    def __init__(self):
        self.Ut = Utility()

    def get_faculty(self):
        print("Please provide information about the faculty: ")
        fclt = Faculty()
        flag = False
        while not flag:
            try:
                name = input('Username: ')
                fclt.username = name
                password = input('Password: ')
                fclt.password = password
                subj = input('Subject: ')
                fclt.subject = subj
                des = input('Designation: ')
                fclt.designation = des
                flag = True
            except Exception as e:
                print(str(e))
        return fclt

    def get_student(self):
        print("Please Provide information about the student")
        std = Student()
        flag = False
        while not flag:
            try:
                name = input('Username: ')
                std.username = name
                password = input('Password: ')
                std.password = password
                std.semester = self.Ut.validate_Semester()
                std.cgpa = self.Ut.validate_CGPA()
                std.degree = self.Ut.validate_degree()
                flag = True
            except Exception as e:
                print(str(e))
        return std

    def get_course(self):
        c_name = input('Enter course name: ')
        return c_name
    def update_std(self,std):
        if std:
            updated_std = Student()
            num= None
            cgpa = float(std[0][1])
            deg = std[0][2]
            sem = int(std[0][0])
            print("CGPA is: ",cgpa)
            print("Do you want to update")
            print("1.   update")
            print("2.   skip")
            num = input("Your Selection: ")
            num = self.Ut.validate_manu(num, "1", "2")
            if num == '1':
                cgpa = self.Ut.validate_CGPA()
            print("\nDegree is: ",deg)
            print("Do you want to update")
            print("1.   update")
            print("2.   skip")
            num = input("Your Selection: ")
            num = self.Ut.validate_manu(num, "1", "2")
            if num == '1':
                deg = self.Ut.validate_degree()
            print("\nSemester is: ",sem)
            print("Do you want to update")
            print("1.   update")
            print("2.   skip")
            num = input("Your Selection: ")
            num = self.Ut.validate_manu(num, "1", "2")
            if num == '1':
                sem = self.Ut.validate_Semester()
            updated_std.cgpa = cgpa
            updated_std.semester= sem
            updated_std.degree = deg
            return updated_std
        else:
            print("No Student Found to update!")
            return None
    def update_faculty(self, fclt):
        if fclt:
            updated_fclt = Faculty()
            num= None
            subject = fclt[0][1]
            designation = fclt[0][0]
            print("Designation is: ",designation)
            print("Do you want to update")
            print("1.   update")
            print("2.   skip")
            num = input("Your Selection: ")
            num = self.Ut.validate_manu(num, "1", "2")
            if num == '1':
                designation = input("Designation: ")
            print("\nSubject is: ",subject)
            print("Do you want to update")
            print("1.   update")
            print("2.   skip")
            num = input("Your Selection: ")
            num = self.Ut.validate_manu(num, "1", "2")
            if num == '1':
                subject = input("Subject: ")
            updated_fclt.designation= designation
            updated_fclt.subject = subject
            return updated_fclt
        else:
            print("No Faculty Found to update!")
            return None
    def chose_btw_std_fclt(self):
        print("1.    Student")
        print("2.    Faculty")
        num = input("Your Selection: ")
        return self.Ut.validate_manu(num, "1", "2")

    def get_login(self):
        username = input("Username: ")
        password = input("Password: ")
        return username, password

    def std_manu(self):
        print("1.   View his/her profile")
        print("2.   Edit his/her profile")
        print("3.   Delete his/her profile")
        print("4.   Add Course(student_id, course_name)")
        print("5.   Delete Course (student_id, course_name)")
        print("6.   GetStudentList(string course_name)")
        print("7.   Exit")
        num = input("Your Selection: ")
        return self.Ut.validate_manu(num, "1", "7")
    def fclt_manu(self):
        print("1.   View his/her profile")
        print("2.   Edit his/her profile")
        print("3.   Delete his/her profile")
        print("4.   Exit")
        num = input("Your Selection: ")
        return self.Ut.validate_manu(num, "1", "4")
    def show_std_list(self, list_std):
        for std in list_std:
            print("Username: ",std[0], " Password: ", std[1]," CGPA: ", std[2], " Semester: ", std[3]," Degree: ",std[4], " Course: ", std[5])
    def show_std(self, std):
        if std:
            print("ID: ",std[0][3], " Degree: ",std[0][2] ," CGPA: ", std[0][1], " Semester: ", std[0][0])
        else:
            print("None")
    def show_fclt(self,fclt):
        if fclt:
            print("ID: ",fclt[0][2], " Subject: ",fclt[0][1] ," Designation: ", fclt[0][0])
        else:
            print("None")
    def printMSG(self, msg):
        print(msg)
    def startup(self):
        print("1.   Sign in")
        print("2.   Register")
        print("3.   Exit")
        num = input("Your Selection: ")
        return self.Ut.validate_manu(num, "1", "3")