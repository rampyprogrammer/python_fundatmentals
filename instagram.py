class vehichle1:
    def __init__(self):
        self.speed1='10km/hr'
        
    def cycle(self):
        print('cycle runs 10km/hr')
        
class vehichle2(vehichle1):
    def __init__(self):
        super().__init__()
        self.speed2='80km/hr'
        
    def  bike(self):
        print("the bike runs at the speed of 100km/hr")
        
class vehichle3(vehichle2):
    def __init__(self):
        super().__init__()
        self.speed3='120km/hr'
        
    def car(self):
        print("the car has more featurs than bike ")
        
ob1=vehichle3()
print("attributes of class car-->",ob1.__dict__)
ob1.cycle()
ob1.bike()
ob1.car()
