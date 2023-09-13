def prime(num,i):
    
    if i==1:
        return 1
    if num%i==0:
        return 3
        
    return prime(num,i-1)

num =int(input("num :"))

ind=prime(num,num-1)
if ind==1:
    print("its a prime number")
else:
    print("its not prime")