l1=[10,20,30,40,50,60]

try:
    i=int(input("index :"))
    if i>=0 and i<=len(l1)-1 or i>=-len(l1) and i>=-1:
        pass
    else:
        raise IndexError
except ValueError as e:
    print(e)
    print("value must be int")
except ZeroDivisionError as e:
    print(e)
    print('denominater must not be zero')
# except IndexError as e:
#     print(e)
except:
    print("some error occured")
    
else:
    print(l1[i])
finally:
    print("completed")