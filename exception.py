#handling multiple exception in try block
print("start")
try:
    a=int(input("a :"))
    b=int(input("b :"))
    c=a/b
except ValueError as e:
    print(e)
    print('value must be int')
except ZeroDivisionError as e:
    print(e)
    print('denominater must not be zero')
except:
    print("some error occured")
else:
    print(c)
finally:
    print("completed")