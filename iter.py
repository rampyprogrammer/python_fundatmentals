class myIterator:
    def __init__(self,max):
        self.max=max
        
    def __iter__(self):
        self.a=0
        return self
    def __next__(self):
        if self.a<=self.max:
            res=self.a+3
            self.a+=1
            return res
        else:
            raise StopIteration
obj=myIterator(12)
result=iter(obj)
for i in range(10):
    print(next(result))
print(type(result))