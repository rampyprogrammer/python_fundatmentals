# n=int(input("n :"))
# if n==1:
#     print("1 is a not a prime number")
#     exit()
# for i in range(2,n):
#     if n%2==0:
#         print(n,' is not a prime number')
#         # break

# else:
#     print(n," is a prime number")
def fabinacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fab=fabinacci()
for i in range(5):
    print(next(fab) )      
        
    