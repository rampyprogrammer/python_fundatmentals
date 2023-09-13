n=int(input("n:"))
v2=(90)-(n-1)
a=v2
for i in range(n):
    
    
    v1=a+i
    for j in range(n):
            if i==0 and j==0:
                print(chr(v2),end=" ")
        
        
            elif i==j:
                print(chr(v2+i-1),end=" ")
                # v2+=i-1
                
            elif i>=j:
                print(chr(v1),end=" ")
            
                        
    print()