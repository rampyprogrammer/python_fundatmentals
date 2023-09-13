class std:
    roll_no=1
    
    @classmethod
    def changeRoll(cls):
        cls.roll_no+=1
        
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        self.__rollNum=std.roll_no
    def setname(self,name,age):
        self.__name=name
        self.__age=age
        self.
        
        
    def display(self):
        print(f"""
              name  :-  {self.name}
              age   :-  {self.age}
              rollno:-  {self.roll_no}""")
o1=std("rama",18)
o1.display()
std.changeRoll()
o1.display()
std.changeRoll()
o1.display()
std.changeRoll()
o1.display()
        