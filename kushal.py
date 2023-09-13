#logics to check prime num or not 
# n=int(input("n :"))
# count=0
# for i in range(1,n+1):
    
#     if n%i==0:
#         count+=1
# if count==2:
#     print('it is a prime number')
# else:
#     print("it is not prime number")
    
     #using recursion
# def prime(n,i=2):
#     if n<2:
#         return False
#     if i<n:
#         if n%i==0:
#             return 'not a prime'
#         return prime(n,i+1)
#     return f"{n} is a prime num"
# print(prime(10))

# n=int(input(" N :"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
    
# print(fact)

n=int(input("n :"))
s=0
a=n
while n>0:
    rem=n%10
    fact=1
    for i in range(rem,1,-1):
        fact*=i
    s+=fact
    