class A:
    def __init__(self):
        self.a=10
        self.b=20
        
    def he(self):
        print("i am from class A")
        
class B(A):
    def __init__(self):
        super().__init__()
        self.x=100
        self.y=200
        
    def she(self):
        print("hey i am from class B")
o1=B()
o1.he()
o1.she()
print('attributes of class B-->',o1.__dict__)

