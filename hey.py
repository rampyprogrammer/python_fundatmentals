class engine:
    def __init__(self,speed,name):
        self.speed=speed
        self.name=name

    def evaluate(self):
        if self.speed<=80 and self.speed>45:
            print("average speed")
        elif self.speed<45:
            print("below avg speed")
        else:
            print("speed is over")
class car:
    def __init__(self,speed,name,color,price):
        self.speed=speed
        self.name=name
        self.color=color
        self.price=price
        self.obj=engine(self.speed,self.name)
        
    def details(self):
        print(f"speed :{self.speed}\nname of car{self.name}\ncolor :{self.color}\nprice :{self.price}")
        
Car=car(90,"FERARI","black","30000000")
Car.obj.evaluate()
Car.details()
        
