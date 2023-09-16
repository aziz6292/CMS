# BCSF19A026
# Abdul Aziz

from view import View
from model import Model

class Controller:
    def __init__(self, host='localhost', user='root', password='Anonymous', db='fcit'):
        self.view = View()
        self.model = Model(host, user, password, db)
        if not self.model.con:
            raise Exception("invalid connection info")

    def startup_manu(self):
        while True:
            num = self.view.startup()
            if num == '1':
                self.login()
            elif num == '2':
                self.Register()
            elif num == '3':
                self.view.printMSG("Thank You!")
                exit()
            else:
                self.view.printMSG("Invalid option\n")
            self.view.printMSG("\n")

    def Register(self):
        n = self.view.chose_btw_std_fclt()
        if n == '1':
            std = self.view.get_student()
            flag = self.model.registerStudent(std)
            if flag:
                self.view.printMSG("Student Successfully Registered!\n")
            else:
                self.view.printMSG("OOPS! Failure in Student Registration\n")
        else:
            fclt = self.view.get_faculty()
            flag = self.model.registerFaculty(fclt)
            if flag:
                self.view.printMSG("Faculty Successfully Registered!\n")
            else:
                self.view.printMSG("OOPS! Failure in Faculty Registration\n")

    def login(self):
        username, password = self.view.get_login()
        id_verified = self.model.authenticate_user(username, password)
        if id_verified:
            self.view.printMSG("Authentication successful!")
            n = self.view.chose_btw_std_fclt()
            if n == '1':
                flag = self.model.as_student(id_verified)
                if flag:
                    while True:
                        n = self.view.std_manu()
                        if n == '1':
                            self.view_std_profile(username, password)
                        elif n == '2':
                            self.edit_std_profile(username, password)
                        elif n == '3':
                            self.dlt_std_profile(username, password)
                            break
                        elif n == '4':
                            self.add_course(id_verified, self.view.get_course())
                        elif n == '5':
                            self.dlt_course(id_verified, self.view.get_course())
                        elif n == '6':
                            self.get_all_student()
                        else:
                            break
                        self.view.printMSG("\n")
                else:
                    self.view.printMSG("OOPS! no such student found\n")
            elif n == '2':
                flag = self.model.as_faculty(id_verified)
                if flag:
                    while True:
                        n = self.view.fclt_manu()
                        if n == '1':
                            self.view_fclt_profile(username, password)
                        elif n == '2':
                            self.edit_fclt_profile(username, password)
                        elif n == '3':
                            self.dlt_fclt_profile(username, password)
                            break
                        else:
                            break
                        self.view.printMSG("\n")
                else:
                    self.view.printMSG("OOPS! no such faculty found\n")
            else:
                self.view.printMSG("Invalid option\n")
        else:
            self.view.printMSG("Authentication Failed")
        self.view.printMSG("\n")
    def view_std_profile(self, username, password):
        std = self.model.get_student(username, password)
        if std:
            self.view.show_std(std)
        else:
            self.view.printMSG("No Such Student Found")

    def view_fclt_profile(self, username, password):
        fclt = self.model.get_faculty(username, password)
        if fclt:
            self.view.show_fclt(fclt)
        else:
            self.view.printMSG("No Such Faculty Found")

    def edit_std_profile(self, username, password):
        std = self.model.get_student(username,password)     
        std = self.view.update_std(std)
        flag = self.model.update_student(username, password, std)
        if flag:
            self.view.printMSG("Student Profile Updated Successfully")
        else:
            self.view.printMSG("Failure in Student Profile Updating")

    def edit_fclt_profile(self, username, password):
        fclt = self.model.get_faculty(username, password)
        fclt = self.view.update_faculty(fclt)
        flag = self.model.update_faculty(username, password, fclt)
        if flag:
            self.view.printMSG("Faculty Profile Updated Successfully")
        else:
            self.view.printMSG("Failure in Faculty Profile Updating")

    def dlt_std_profile(self, username, password):
        flag = self.model.delete_student(username, password)
        if flag:
            self.view.printMSG("Student Profile Deleted Successfully")
        else:
            self.view.printMSG("Failure in Student Profile Deleting")

    def dlt_fclt_profile(self, username, password):
        flag = self.model.delete_faculty(username, password)
        if flag:
            self.view.printMSG("Faculty Profile Deleted Successfully")
        else:
            self.view.printMSG("Failure in Faculty Profile Deleting")

    def add_course(self, std_id, course_name):
        flag = self.model.add_course(std_id, course_name)
        if flag:
            self.view.printMSG("Course Added to Student Profile Successfully")
        else:
            self.view.printMSG("Failure in Adding New Course")

    def dlt_course(self, std_id, course_name):
        flag = self.model.delete_course(std_id, course_name)
        if flag:
            self.view.printMSG("Course Deleted Successfully")
        else:
            self.view.printMSG("Failure in Deleting Course")

    def get_all_student(self):
        course_name = self.view.get_course()
        std_list = self.model.get_student_list(course_name)
        if std_list:
            self.view.show_std_list(std_list)
        else:
            self.view.printMSG("No student enrolled to such course")

print("Please make connection to your Database Server")
flag = True
user = None
while flag:
        host = input("host i.e (localhost): ")
        user = input("user i.e (root): ")
        password = input("password: ")
        db = input("database i.e (fcit): ")
        print("\n")
        try:
            user = Controller(host, user, password, db)
            flag = False
        except Exception as e:
            print("Error in connection: ",str(e)+'\n')
user.startup_manu()

