# # l1=[100,200,300,400]

# # #creating an iterator for l1
# # it1=l1.__iter__()
# # print(it1)
# # print(type(it1))
# l1=[100,200,300,400]
# #creating an iterator for l1
# it1=l1.__iter__()
# print(dir(l1))
# print("_"*99)
# print(dir(it1))
# class five:
#     def __init__(self):
#         self.s1=0
    
#     def __iter__(self):
#         self
#     def __next__(self):
#         t=self.s1
#         if t<5:
#             self.s1+=1
#             return t
#         else:
#             raise StopIteration
# obj=five()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# l1=[100,200,300,400]
# it1=iter(l1)
# print(it1)

# print(next(it1))      
# print(next(it1))      
# print(next(it1))      
# print(next(it1))      
# print(next(it1))      
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
my_iterator=MyIterator([1,23,3,4,5,6,7])
for items in my_iterator:
    print(items,end=' ')

