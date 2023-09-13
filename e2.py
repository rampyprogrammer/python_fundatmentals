#custome exception
class MyError(Exception):
    pass

try:
    val=int(input("val :"))
    if val>10:
        raise MyError
except MyError:
    print("the value must not be greater than 10")
except ValueError as e:
    print(e)
    print("value must be int")
except ZeroDivisionError as e:
    print(e)
    print('denominater must not be zero')
except:
    print('some error accured')
else:
    print(val) 
    
finally:
    print('complted')
print("end")