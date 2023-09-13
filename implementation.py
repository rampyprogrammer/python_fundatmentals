from abstaction import Calci

class caluculation(Calci):
    def sum(self,*arg):
        res=0
        for i in arg:
            res+=i
        return res
    def product(self,*arg):
        pro=1
        for i in arg:
            pro*=i
        return pro
    
    