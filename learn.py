class A:
    def __init__(self,a):
        self.a=a
        
    def fun(self):
        print('i am fun of A')
        print(f'a-->{self.a}')
        
class B:
    def __init__(self,b):
        self.b=b
        
    def fun(self):
        print("i am fun of B")
        print(f"b-->{self.b}")
        
class C(A,B):
    def __init__(self,a,b):
        A.__init__(self,a=a)
        B.__init__(self,b=b)
        
    def fun(self):
        A.fun(self)
        B.fun(self)
obj=C(123,125)
obj.fun()
