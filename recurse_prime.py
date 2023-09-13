# def is_prime(n,i=2):
#     if n<=2:
#         return n==2
#     if n%i==0:
#         return False
#     if i*i>n:
#         return True
#     return is_prime(n,i+1)
    
# def  print_prime(start,end):
#     if start>end:
#         return
#     if is_prime(start):
#         print(start)
#     print_prime(start+1,end)

# print_prime(1,100)

def fun(n):
    if n<=2:
       return n==2
print(fun(2))