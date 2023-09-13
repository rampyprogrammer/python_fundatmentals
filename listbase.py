# # # # list=[1,542,33,44,55,567,100]
# # # # list.sort()
# # # # print("min value in list",list[0])
# # # # print("max value in list",list[-1])
# # # mylist=[1,2,3,4,5,6]
# # # s=len(mylist)
# # # print(mylist)
# # # temp=mylist[0]
# # # mylist[0]=mylist[s-1]
# # # mylist[-1]=temp
# # # print(mylist)
# # mylist=[1,2,3,4,5,6]
# # print(mylist)
# # mylist[0],mylist[-1]=mylist[-1],mylist[0]
# # print(mylist)

# class one:
#     a=100
#     def fun(self):
#         print("hello i am instance method")
#         a=200
# # one.fun()
# print(one.a)
# ob=one()
# ob.fun()
# print(one.a)

class employee:
    A=100
    def __init__(self,empname,empid):
        self.empname=empname
        self.empid=empid
        
    def update(self,empname):
        self.empname=empname
    def updateclass(self,value):
        self.__class__.A=value
        
    # def delete(self):
    #     del self.empname
    def deleteclasvar(self):
        del self.__class__.A
ob=employee('rama',1244)
print(ob.empname)
print(ob.empid)
ob.update("huligappa")
print(ob.empname)
print(ob.empid)
print(employee.A)
ob.updateclass(12)
print(employee.A)
print(ob.A)
# ob.deleteclasvar()
# print(employee.A)
employee.update('ayo',134)
# print(ob.empname)
# ob.delete()
# print(ob.empname)



