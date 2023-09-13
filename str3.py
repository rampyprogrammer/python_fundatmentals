# s1="iron man"
# print(s1[::-1])
l1=['man$@','D@##on','a$b:5',100]
specialChar="!@#$%^&*()"
for i in l1:
    c=0
    for j in str(i):
        c+=1
        count=0
        if j in specialChar and c%2==1:  
            count+=1
print(count)
    
        
        