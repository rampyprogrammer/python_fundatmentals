class Student:
    def __init__(self,name,age,gender):
        self.__name=name
        self.__age=age
        self.__gender=gender
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getGender(self):
        return self.__gender
    
    def setName(self,name):
        self.__name=name
    def setAge(self,age):
        self.__age=age
        
    def setGender(self,gender):
        self.__gender=gender
ob=Student("rama",21,"male")
print(ob.getName())
print(ob.getAge())
print(ob.getGender())

print("modifying the attributes of student")
ob.setAge(20)
ob.setName("jaanu")
ob.setGender("female")
print(ob.getName())
print(ob.getAge())
print(ob.getGender())


        
        
    