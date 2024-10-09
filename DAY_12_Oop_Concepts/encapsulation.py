class clsSchool:
    school_name="Green Valley High School"
    strName=""
    student_id=""
    maths_marks = 0
    science_marks = 0
    english_marks = 0
    average = 0   
    def __init__(self,name,id,marks1,marks2,marks3):
        self.strName= name

        self.student_id=id
        self.maths_marks=marks1
        self.science_marks=marks2
        self.english_marks=marks3
        self.average=self.calculate_average()
        
        
    def setValue(self,name,clsSchool,id,marks1,marks2,marks3,averge1):
        self.strName= name
        self.school_name=clsSchool
        self.student_id=id
        self.maths_marks=marks1
        self.science_marks=marks2
        self.english_marks=marks3
        self.average=self.calculate_average()
        
    def calculate_average(self):
        return (self.maths_marks + self.science_marks + self.english_marks) / 3
        
    def display_student(self):
        print("Name: ",self.strName)
        print("School: ",clsSchool.school_name)
        print("student_id: ",self.student_id )
        print("Maths: ",self.maths_marks)
        print("Science: ",self.science_marks)
        print("English: ",self.english_marks)
        print("Average",self.average)
        
if __name__=="__main__":
    objstudent1=clsSchool("Vaibhav",1,56,89,56)
    objstudent2=clsSchool("Vaiashali",2,76,90,86)
    objstudent1.display_student()
    objstudent2.display_student()
    
def find_topper(students):
    topper = students[0]
    for student in students:
        if student.average > topper.average:
            topper = student
    return topper
    
    
lstObjList=[]
lstObjList.append(objstudent1)
lstObjList.append(objstudent2)
for item in lstObjList:
    item.display_student()
    topper = find_topper(lstObjList)
    if topper:
        print("\nTopper of the Class:")
        topper.display_student()
    else:
        print("No students available.") 