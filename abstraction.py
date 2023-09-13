from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    
    def method2(self):
        print("i am spider man")
        
    @abstractmethod
    def method3(self):
        pass
    
    @abstractmethod
    def method4(self):
        pass
    
class B(A):
    def method1(self):
        print("i am abstract method one from the abstract class")
    def method3(self):
        print("i am abstract method two from abstract class")
    def method4(self):
        print("i am spiderman 2")
        
    
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()
obj1.method4()