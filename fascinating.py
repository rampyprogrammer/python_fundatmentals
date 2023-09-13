n=int(input("n: "))
s1=str(n)+str(n*2)+str(n*3)
for i in "123456789":
    if str(i) not in s1 and s1.count !=1:
        print( "its not fascinating")
        break
else:
    print("its a fascinating")
    
    
    