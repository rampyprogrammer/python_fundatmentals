class Engine:
    def __init__(self, model, horsepower):
        self.model = model
        self.horsepower = horsepower

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.obj=Engine("V8", 450)

    def start(self):
        print(f"{self.make} {self.model} with {self.engine.horsepower} horsepower engine has started.")

# engine = Engine("V8", 450)
car = Car("Ferrari", "F8 Tributo", 2022 )
car.start()
