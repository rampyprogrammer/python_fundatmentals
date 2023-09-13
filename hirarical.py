class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def exerise(self):
        print("to be fit a man should do workouts")

    def eat(self):
        print("to live  a man shoul eat 3 times a day")

class Student(Person):
    def __init__(self,rollNo,name,age,gender):
        super().__init__(name=name,gender=gender,age=age)
        self.rollNo=rollNo

    def Exams(self):
        print("to get a degree you need to write exam and you should pass it")

class Employee(Person):
    def __init__(self,Id,name,age,gender):
        super().__init__(name=name,age=age,gender=gender)
        self.Id=Id

    def work(self):
        print("to get sal at month end you should work at office")
class worker1(Employee):
    def __init__(self,Id,age,gender,name):
        super().__init__(Id,name,age,gender)

    

    def labour(self):
        print("i am working as a labour")
obj =Employee("id5354","rakesh",34,'male')

print(obj.name)
print(obj.age)
print(obj.gender)
obj.eat()
obj.exerise()
obj.work()

obj3=worker1(9909,43,'male','suri')
obj3.

obj2=Student("498","rama",22,'male')

print(obj2.name)
print(obj2.age)
print(obj2.gender)
obj2.eat()
obj2.exerise()
obj2.Exams()

