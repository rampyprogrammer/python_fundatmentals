# def prime(n,i):
#     if n==1:
#         return 1
#     if n%i==0:
#         return 0
#     return prime(n,i-1)



# list=[x for x in range(int(input('from :')),int(input("to :")))]
# for n in list:
#     ind =prime(n,n-1)
    
#     if ind==0:
#       pass
#     else:
#         print("its a prime")
list=[x for x in range(int(input('from :')),int(input("to :")))]
for n in list:
   

    for i in range(2,n-1):
        
        if n%i==0:
            pass
        else:
            print(n)
            
        