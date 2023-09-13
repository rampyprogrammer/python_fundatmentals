def revrese(str):
    if len(str)==1:
        return str
    else:
        return revrese(str[1:]) + str[0]
str=input("enter the string here :")
print(revrese(str))