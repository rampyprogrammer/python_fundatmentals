class student:
    def __init__(self,name,age,address):
        self.__name=name
        self.__age=age
        self.__address=address
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    def getaddress(self):
        return self.__address
    def setname(self,name):
        self.__name=name
    def setage(self,age):
        self.__age=age
    def setaddress(self,address):
        self.__address=address
        
    
o1=student('rama',22,'dubai')
print(o1.getname())
print(o1.getage())
print(o1.getaddress())
print('res modifying')
o1.setname('prakash')
o1.setage(20)
o1.setaddress('bengaluru')
print(o1.getname())
print(o1.getage())
print(o1.getaddress())




