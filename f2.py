def rec(a,b):
    if a==0:
        return b
    else:
        return rec(a-1,a+b)
print(rec(8,12))
