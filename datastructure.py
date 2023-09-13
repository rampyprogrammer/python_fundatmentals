def sum_of_num(num,sum=0):
    if num==0:
        return sum
    else:
        sum=num%10
        return sum_of_num(num//10) + sum
        
    
    
        
        


print(sum_of_num(2345))