# # # # # list=["hello",10,20,30,20,40,43,40]
# # # # # l2=[]
# # # # # for ele in list:
# # # # #     if list.count(ele)>1 and ele not in l2:
# # # # #         l2.append(ele)
# # # # # print(l2)

# # # # ##or
# # # # l=["hello",10,20,30,20,40,43,40]
# # # # l1=[]
# # # # for i in range(len(l)):
# # # #     for j in range(i+1,len(l)):
# # # #         if l[i]==l[j] and l[i] not in l1:
# # # #             l1.append(l[i])
# # # # print(l1)
            
# # # l=["hello",10,20,30,20,40,43,40]
# # # print(l)
# # # l2=list(set(l))
# # # print(l2)

# # l=["hello",10,20,30,20,40,43,40]
# # print(l)
# # # l2=[]
# # # for i in l:
# # #     if i not in l2:
# # #         l2.append(i)
# # # print(l2)
# # list=[]
# # [list.append(ele) for ele in l if ele if ele not in list ]
# # print(list)
# str="a2b3c4"
# # op="aabbbcccc"
# str1=""
# for i in str:
#     if i.isalpha():
#         char=i
#     else:
#         str1+=char*int(i)
# print(str1)
s="we are good"
d=""
s1=s.split()
for i in s1:
    if len(i)>1:
        d+=i[-1]+i[1:-1]+i[0]+" "
    else:
        d+=i
        
    
    
    
print(d)
    