class AgeLessesrError(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.message=message
class AgeGreaterError(Exception):
    def __init__(self,message):
        self.message=message

try:
    age=int(input("age :"))
    if age>45:
        raise AgeGreaterError("the age shouln't be greater than 45")
    elif age<20:
        raise AgeLessesrError("the age shouldn't be lesser than 20")
# except ValueError as e:
#     print(e)
except AgeLessesrError as e:
    print(e)
    print('not eligibel')
except AgeGreaterError as e:
    print(e)
    print('not eligible because man became hold')
except Exception as e:
    print('some error occured : ',e)
else:
    print("eligible candidate to do that....")
finally:
    print("kelsa katham ho gaya waiting for the result")