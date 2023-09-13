class insta1:
    def __init__(self):
        self.version=0.1
    
    def photo_uplopad(self):
        print("photo posted succesfully")
class insta2(insta1):
    def __init__(self):
        super().__init__()
        self.version2=0.2
    def reels(self):
        print("here we can watch reels and upload")
class insta3(insta2):
    def __init__(self):
        super().__init__()
        self.version3=0.34
    def filters(self):
        print("hi here we can use filters like when i get married")
        
obj=insta3()
print(obj.version)
obj.photo_uplopad()

print(obj.version2)
obj.reels()

print(obj.version3)
obj.filters()

        