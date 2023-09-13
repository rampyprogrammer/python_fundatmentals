n=int(input("enter num :"))
v1=ord("E")
v2=5
for i in range(n):
    for j in range(n):
        if i>=j:
            if i%2==0:
                print(chr(v1),end=" ")
                
            else:
                print(v2,end=" ")
            
        else:
            print(" ",end=" ")
    if i%2==0:
        v1-=1
        if v1<ord("A"):
            v1=ord("Z")
        v2-=1
        if v2<1:
            v2=9
        
    print()