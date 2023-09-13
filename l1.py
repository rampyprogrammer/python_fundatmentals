# n=int(input(" N :"))
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     temp=a
#     a=b
#     b=b+temp
#     #or a,b=b,a+b

# n=int(input("n :"))
# # c=0
# # for i in range(1,n+1):
# #     if n%i==0:
# #         c+=1
# if n%2==0:
#     print(f"{n} is not a prime number")
# else:
#     print(f"{n} is  a prime number")
    
n=int(input("n :"))
if n==1:
    print("1 is not a prime num")
    exit()
for i in range(2,n):
    if n%i==0:
        print(f"{n} is not a prime num")
        # break
else:
    print(f"{n} is a prime number")
    