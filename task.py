class vehicilqueue:
    def __init__(self):
        self.cars=[]
        self.bikes=[]
    def enque(self,type,vehicel):
        if type=="car":
            self.cars.append(vehicel)
        elif type=="bike":
            self.bikes.append(vehicel)
    def display(self):
        print(self.cars,self.bikes)
    def bikedequeue(self):
        return self.bikes.pop(0)
    def cardequeue(self):
        return self.cars.pop(0)
        
ob=vehicilqueue()
ob.enque("car","Ferrari F8")
ob.enque("car","Benz")
ob.enque("car","Bugati")
ob.enque("car","rangerover")
ob.enque("bike","ns120")
ob.enque("bike","Raider")
ob.enque("bike","pulser")
ob.enque("bike","Honda")
ob.display()
ob.cardequeue()
ob.display()