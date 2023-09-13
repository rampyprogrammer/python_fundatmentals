# n=int(input(" enter num : "))
# def prime(n,i=2):
#     if n<=2:
#         return False
#     if n%i==0:
#         return "not a prime number"
#     if i*i>n:
#         return "prime number"
#     return prime(n,i+1)
# print(prime(n))
     #iterator a sample example
     
class MyIterator:
    def __init__(self,data):
        self.index=0
        self.data=data
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result=self.data[self.index]
        self.index+=1
        return result
my_iterator=MyIterator([1,2,3,'virat','vs'])
for i in my_iterator:
    print(i,end=" ")
        