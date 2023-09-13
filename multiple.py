class Puma:
    def __init__(self):
        self.company_name='puma'
        
    def manfacture(self):
        print("puma brand shoes available here")
    
class Adidas:
    def __init__(self):
        self.company_Name2="Adidas"
    def producing(self):
        print("adidas branded shirts are available here ")

class ShareMarket(Puma,Adidas):
    def all(self):
        print("*"*30+"share market"+"*"*30)
        print("All branded shoes are available here :")
        Puma.__init__(self)
        Adidas.__init__(self)
obj=ShareMarket()
if __name__=="__main__":
    obj.all()
# print("company name  : ",obj.company_name)
    obj.manfacture()

# print("company name : ",obj.company_Name2)
    obj.producing()
else:print("you wrote fucking worse code")
    