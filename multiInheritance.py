class Insta1:
    def __init__(self):
        self.version1 = "2.O"

    def Post(self):
        print(f"this {self.version1} will allow us to post our photos")

class Insta2(Insta1):
    def __init__(self):
        super().__init__()
        self.version2 ="3.O1"

    def Filter(self):
        print(f"hey this {self.version2} verison provides filters while taking pictures")

class Insta3(Insta2):
    def __init__(self):
        super().__init__()
        self.version3 ="5.O3"

    def Reels(self):
        print(f"hey this {self.version3 } verison provides a feature of watching reels making reels by doing this we can explore our acting in reels")

obj=Insta3()
obj.Post()
obj.Filter()
obj.Reels()


        