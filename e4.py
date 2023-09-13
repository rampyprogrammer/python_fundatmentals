class AgeLesserException(Exception):
    def __init__(self,message):
        super().__inti__(message)
        self.message=message

class AgeGreaterException(Exception):
    def __init__(self,message):
        # super().__inti__(message)
        self.message=message

try:
    age=int(input("enetr the age : "))
    if age>45:
        raise AgeGreaterException("the age shouldnot be greater than  45")
    if age<20:
        raise AgeLesserException("age must not be lesser than 20...")
except AgeLesserException as e:
    print(e)
except AgeGreaterException as e:
    print(e)
except Exception as e:
    print(" the error occured : ",e)
else:
    print("this person is eligible for the fuc*** a aunty")
finally:
    print("finally the aunty is fucked by raamu")
