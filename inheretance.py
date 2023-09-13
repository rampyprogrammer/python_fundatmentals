class A:
    a=10
    b=20
    def m1(self):
        print('i am  m1 of class A')
    
class B(A):
    x=100
    y=200
    def m2(self):
        print("i am m2 of class B")
        
o1=B()
print('attributes of class b-->',o1.__dict__)
print(o1.a)
print(o1.b)
o1.m1()
o1.m2()
