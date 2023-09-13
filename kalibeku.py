class Subject:
    def __init__(self,sub_name):
        self.sub_name=sub_name
        
class Maths(Subject):
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Subject.__init__(self,sub_name="maths")
    def details(self):
        print(f"name :{self.name}\n marks :{self.marks}")
        
class physics(Subject):
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Subject.__init__(self,sub_name="physics")
        
    def details2(self):
        print(f"")
        
obj=
        

