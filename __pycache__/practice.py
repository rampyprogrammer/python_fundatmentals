n=int(input("n:"))   
for in range(n):
    val=ord("A")+(n-1-i)
    if val<ord("A"):val=ord("Z")
    for j in range(i+1):
        print(chr(val),end=" ")
    print()