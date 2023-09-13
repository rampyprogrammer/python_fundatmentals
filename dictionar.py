n=int(input())
s=0
for i in str(n):
    fact=1
    for j in range(int(i),1,-1):
        fact*=j
    
    s+=fact

if s==n:
    print("strong")
else:
    print("not strong")