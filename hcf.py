a=int(input("a :"))
b=int(input("b: "))
for i in range(a,0,-1):
    if a%i==0 and b%i==0:
        print(i)
        break
        
