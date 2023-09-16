# BCSF19A026
# Abdul Aziz
import pymysql
from student import Student
from faculty import Faculty
from course import Course


class Model:
    def __init__(self, host='localhost', user='root', password='Anonymous', db='fcit'):
        self.host = host
        self.user = user
        self.password = password
        self.database = db
        self.con = None
        self.cursor = None
        try:
            self.con = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            self.cursor = self.con.cursor()
        except Exception:
            pass

    def __del__(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.con:
                self.con.close()
        except Exception:
            pass

    def authenticate_user(self, username, password):
        try:
            sql = "select ID from fcit.user where USERNAME=%s and PASSWORD=%s"
            arg = (username, password)
            self.cursor.execute(sql, arg)
            id = self.cursor.fetchone()
            if id:
                id = int(str(id[0]))
                return id
            else:
                raise Exception("invalid username or password")
        except Exception as e:
            print(str(e))
            return None
    # def as_student(self, id):
    #     try:
    #         sql = "select * from fcit.student where STD_ID =%s"
    #         arg = (id)
    #         self.cursor.execute(sql, arg)
    #         std = self.cursor.fetchone()
    #         if std:
    #             return True
    #         else:
    #             raise Exception("invalid username or password")
    #     except Exception as e:
    #         print(str(e))
    #         return False
    # def as_faculty(self, id):
    #     try:
    #         sql = "select * from fcit.faculty where FCLT_ID =%s"
    #         arg = (id)
    #         self.cursor.execute(sql, arg)
    #         fclt = self.cursor.fetchone()
    #         if fclt:
    #             return True
    #         else:
    #             raise Exception("invalid username or password")
    #     except Exception as e:
    #         print(str(e))
    #         return False
    def registerStudent(self, std):
        try:
            sql = "INSERT into fcit.user VALUES('0',%s,%s)"
            arg = (std.username, std.password)
            self.cursor.execute(sql, arg)
            id = self.authenticate_user(std.username, std.password)
            if id:
                sql = "INSERT into fcit.student VALUES(%s,%s,%s,%s)"
                arg = (std.semester, std.cgpa, std.degree, id)
                self.cursor.execute(sql, arg)
                self.con.commit()
                return True
            else:
                raise Exception("Invalid username or password")
        except Exception as e:
            print(str(e))
            return False

    def registerFaculty(self, fclt):
        try:
            sql = "INSERT into fcit.user VALUES('0',%s,%s)"
            arg = (fclt.username, fclt.password)
            self.cursor.execute(sql, arg)
            id = self.authenticate_user(fclt.username, fclt.password)
            if id:
                sql = "INSERT into fcit.faculty VALUES(%s,%s,%s)"
                arg = (fclt.designation, fclt.subject, id)
                self.cursor.execute(sql, arg)
                self.con.commit()
                return True
            else:
                raise Exception("Invalid username or password")
        except Exception as e:
            print(str(e))
            return False

    def get_faculty(self, username, password):
        try:
            id = self.authenticate_user(username, password)
            if id:
                sql = "select * from fcit.faculty where FCLT_ID=%s"
                arg = (id)
                self.cursor.execute(sql, arg)
                data_faculty = self.cursor.fetchall()
                return data_faculty
            else:
                raise Exception("Invalid username or password")
        except Exception as e:
            print(str(e))
            return None

    def get_student(self, username, password):
        try:
            id = self.authenticate_user(username, password)
            if id:
                sql = "select * from fcit.student where STD_ID=%s"
                arg = (id)
                self.cursor.execute(sql, arg)
                std = self.cursor.fetchall()
                return std
            else:
                raise Exception("Invalid username or password")
        except Exception as e:
            print(str(e))
            return None

    def update_faculty(self, username, password, fclt):
        try:
            id = self.authenticate_user(username, password)
            if id:
                sql = "UPDATE fcit.faculty set DESIGNATION=%s, SUBJECT=%s where FCLT_ID=%s"
                arg = (fclt.designation, fclt.subject, id)
                self.cursor.execute(sql, arg)
                self.con.commit()
                return True
            else:
                raise Exception("invalid username or password")
        except Exception as e:
            print(str(e))
            return False

    def update_student(self, username, password, std):
        try:
            id = self.authenticate_user(username, password)
            if id:
                sql = "UPDATE fcit.student SET SEMESTER = %s, CGPA= %s, DEGREE = %s WHERE STD_ID =  %s;"
                arg = (std.semester, std.cgpa, std.degree, id)
                self.cursor.execute(sql, arg)
                self.con.commit()
                return True
            else:
                raise Exception("invalid username or password")
        except Exception as e:
            print(str(e))
            return False

    def delete_faculty(self, username, password):
        try:
            id = self.authenticate_user(username, password)
            if id:
                sql = "delete from fcit.faculty where FCLT_ID=%s"
                arg = (id)
                self.cursor.execute(sql, arg)
                self.con.commit()
                sql = "delete from fcit.user where ID=%s"
                arg = (id)
                self.cursor.execute(sql, arg)
                self.con.commit()
                return True
            else:
                raise Exception("invalid username or password")
        except Exception as e:
            print(str(e))
            return False

    def delete_student(self, username, password):
        try:
            id = self.authenticate_user(username, password)
            if id:
                sql = "delete from fcit.student where STD_ID=%s"
                arg = (id)
                self.cursor.execute(sql, arg)
                self.con.commit()
                sql = "delete from fcit.user where id=%s"
                arg = (id)
                self.cursor.execute(sql, arg)
                self.con.commit()
                return True
            else:
                raise Exception("invalid username or password")
        except Exception as e:
            print(str(e))
            return False

    def add_course(self, id, c_data):
        try:
            sql = "insert into fcit.courses values(%s,%s)"
            arg = (id, c_data)
            self.cursor.execute(sql, arg)
            self.con.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def delete_course(self, id, c_name):
        try:
            sql = "DELETE from fcit.courses where COURSE_NAME=%s and STUDENT_ID=%s"
            arg = (c_name, id)
            self.cursor.execute(sql, arg)
            self.con.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def get_student_list(self, course_name):
        try:
            sql = "select USERNAME, PASSWORD,CGPA,SEMESTER,DEGREE,COURSE_NAME from fcit.user,fcit.student, fcit.courses where STD_ID = ID and COURSE_NAME = %s"
            arg= (course_name)
            self.cursor.execute(sql, arg)
            list_std = self.cursor.fetchall()
            return list_std
        except Exception as e:
            print(str(e))
            return None
