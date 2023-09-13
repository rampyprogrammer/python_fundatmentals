class Students:
    def __init__(self,name,age,roll):
        self.__name=name
        self.__age=age
        self.__roll=roll

    def getName(self):
        return self.__name
    
    def GetAge(self):
        return self.__age
    
    def GetRoll(self):
        return self.__roll
    
    def setName(self,name):
        self.__name=name
    
    def setAge(self,age):
        self.__age=age

    def setRoll(self,roll):
        self.__roll=roll
    
obj=Students("govardhan",34,134)


print(obj.getName())
print(obj.GetAge())
print(obj.GetRoll())

obj.setName("siddu")
obj.setAge(32)
obj.setRoll(520)

print("new student admision")

print(obj.getName())
print(obj.GetAge())
print(obj.GetRoll())