# #printing   fabbinacci num using generator
# def fab_num(nums):
#     a,b=0,1
#     for i in range(nums):
#         yield a 
#         a,b=b,a+b
        
# # gen=fab_num(10)
# # print(gen.__next__())
# # print(gen.__next__())
# # print(gen.__next__())
# # print(gen.__next__())
# for items in fab_num(10):
#     print(items,end=" ")
    
def gen():
    yield 1
    
    yield 2
    yield 3
    yield 4
gen=gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
    