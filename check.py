class std:
    rollNum=1
    @classmethod
    def roll_change(cls):
        cls.rollNum+=1
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.rol=std.rollNum
        
    def println(self):
        print(f"""
             name   :{self.name}
             age    :{self.age}
             roll no:{self.rol}""")
ob1=std("rama",16)
ob1.println()
ob2=std("rama",16)

ob2.println()   




