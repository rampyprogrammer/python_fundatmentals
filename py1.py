class A:
    def method(self):
        print("i am class A")
    
class B:
    def method(self):
        print("i am class B")
class C(A,B):
    def method(self):
        pass
    
o1=C()
o1.method()
