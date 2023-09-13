# # # # # s1= "sp!derMAN is good person"
# # # # # s2=""
# # # # # for i in s1:
# # # # #     if "a" <= i <="z":
        
# # # # #         s2+=chr(ord(i)-32)
    
# # # # #     else:
# # # # #         s2+=i
# # # # # print(s2)

        
# # # # # reversing the string   
# # # # s1="spiderman"
# # # # s2=""
# # # # for i in s1:
# # # #     s2=i+s2

# # # # print(s2)     

# # # s1="spiderman"
# # # s2=""
# # # a=input()
# # # for i in s1[:-1]:
# # #     s2+=i+s1
# # # print(s2) zc

# # s1="spiderman is a good person"
# # print(s1)
# # d1={}
# # for i in s1:
# #     d1[i] = s1.count(i)
# # # print(d1)   
# ###################replace
# s1="spiderman is a good man"
# print(s1)
# s2=""
# i=0
# os=input()
# ns=input()
# while i<len(s1):
#     if s1[i:i+len(os)]==os:
#         s2+=ns
#         i+=len(os)
#     else:
#         s2+=s1[i]
#         i+=1
# print(s2)

        
s1="spider"
l1=[]

for i in range(len(s1)):
        l1+=[s1[:i+1]]
print(l1)
    
    