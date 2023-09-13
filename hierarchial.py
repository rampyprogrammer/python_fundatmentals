class Person:
    def __init__(self,name,age,gender) :
        self.name = name
        self.age = age
        self.gender = gender
        
    def eating(self):
        print("i eat healthy food to be alive")
        
    def excersise(self):
        print("i do excersise 4 days a week")
    
class Student(Person):
    def __init__(self, name, age, gender,sid,rollnum):
        super().__init__(name, age, gender)
        self.sid=sid
        self.rollnum=rollnum
        
    def exam(self):
        print("i need to attend exam to  get digree certificat")
class Employee(Person):
    def __init__(self, name, age, gender,empid,empsal):
        super().__init__(name, age, gender)
        self.empid=empid
        self.empsal=empsal
    def sal(self):
        print("i need to work 8hrs a day to get salary")
if __name__=="__main__":
    print("Student details")
    std=Student("rama",23,'male',6525,143)
    print("student Name    :-",std.name)
    print("student age     :-",std.age)
    print("student gender  :-",std.gender)
    print("student id      :-",std.sid)
    print("roll number     :-",std.rollnum)
    std.eating()
    std.excersise()
    std.exam()

    print("*"*89)

    print("employee details")
    emp=Employee('praveen',45,"male",756,35000)
    print("emp name  :-",emp.name)
    print("emp age   :-",emp.age)
    print("emp gender:-",emp.gender)

    print("emp id    :-",emp.empid)
    print("emp sal   :-",emp.empsal)
    std.eating()
    std.excersise()
    std.exam()


        