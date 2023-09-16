# BCSF19A026
# Abdul Aziz
class Utility:
    def __init__(self):
        pass
    def validate_manu(self, val, start, end):
        while val < start or val> end:
            try: 
                print("Please select in range (", start, '-', end,"): ")
                val = input("Enter a valid value: ")
            except Exception as e:
                    print(str(e))
        return val
    def validate_CGPA(self):
        flag = True
        while flag:
            try:
                cgpa = float(input("CGPA: "))
                if isinstance(cgpa, (float, int)) and cgpa >= 0 and cgpa <= 4:
                    return cgpa
                else:
                    raise Exception ("Invalid CGPA")
            except Exception as e:
                print(str(e))
                flag = True
    def validate_Semester(self):
        while True:
            try:
                sem = int(input("Semester: "))
                if isinstance(sem, int) and sem >= 1 and sem <= 8:
                    return sem
                else: raise Exception ("Invalid Semester")
            except Exception as e:
                print(str(e))
    def validate_degree(self):
        deg = input("Degree: ")
        while deg not in ['BSE', 'BCS', 'BIT', 'BDS']:
            deg = input("Please Enter Degree (BSE, BCS, BIT, BDS): ")
            deg = deg.upper()