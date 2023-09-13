def fun(n,c=0):
    if n>0:
        
        return fun(n-1,c+n)
    return c
print(fun(5))