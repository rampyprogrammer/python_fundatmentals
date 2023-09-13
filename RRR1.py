class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def exercise(self):
        print("exercise")
class student(person):
    def __init__(self, name, age, gender,rollno):
        super().__init__(name, age, gender)
        self.rollno =rollno
    def exam(self):
        print("we need to write exam")
class employee(person):
    def __init__(self,name,age,gender,empid):
        super().__init__(name,age,gender)
        self.empid=empid
    def work(self):
        print("employee will work in office")
c=employee('rama',21,'male',1)
print(c.name)
print(c.age)
print(c.empid)
print(c.gender)
c.work()
c.exercise()