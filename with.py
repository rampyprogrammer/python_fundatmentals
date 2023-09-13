print('start')
a=int(input("a :"))
b=int(input("b :"))
try:
    c=a/b 
except:
    print("denominater must not be zero")
else:
    print(c)
finally:
    print('completd')