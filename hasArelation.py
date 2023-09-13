class heart:
    def __init__(self,name,hbeat):
        self.name=name
        self.hbeat=hbeat

    def analyze(self):
        if self.hbeat>=68 or self.hbeat<=75:
            print(f"{self.name} is normal")
        else:
            print(self.name,"is abnormal")

class patient:
    def __init__(self,name,hbeat,age,gender):
        self.age=age
        self.gender=gender
        self.name=name
        self.hbeat=hbeat
        
        self.obj=heart(self.name,self.hbeat)

    def fun(self):
        print('age: ',self.age)
        print('gende: ',self.gender)
obj1=patient('rama',76,23,'male')
obj1.fun()
obj1.obj.analyze()

        
        
