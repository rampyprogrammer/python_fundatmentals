n=int(input(" n :"))
for i in range(n-1):
    for j in range(2*n-i):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
          print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
        
    
        
        