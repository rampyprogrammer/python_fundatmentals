def register():
    print("""
          -:  FaceBook   sinup  :-""")
    db=open("database.txt","r")
    user_name=input("creat user name  :    ")
    password =input("creat password  :     ")
    confirm_password=input("enter confirm password  :   ")
    
    d=[]
    f=[]
    for i in db:
        a,b=i.split(", ")
        b=b.strip()
        d.append(a)
        f.append(b) 
    data=dict(zip(d, f))
    print(data)   
    # db.close()
    if password != confirm_password:
        print("passwords not matching .. restart")
        register()
    else:
        if len(password)<=6:
            print("password is too short")
            register()
        elif user_name in d:
            print("user name exist..")
            register()
        else:
            db=open("database.txt","a")
            db.write(user_name+", "+password+"\n")
            print("account is successfully created")
            #db.close()


def access():
    db=open("database.txt","r")
    user_name = input("enter your name :  ")
    password = input("enter your password")
    
    if not len(user_name or password)<1:
        d=[]
        f=[]
        for i in db:
            a,b=i.split(", ")
            b=b.strip()
            d.append(a)
            f.append(b) 
        data=dict(zip(d, f))
        
        try:
            if data[user_name]:
                try:
                    if password==data[user_name]:
                        print("login succesfull")
                        print("hi,", user_name)
                    else:
                        print("incorrect password or username")
                except:
                    print("incorrect password or username")
            else:
                print("User name or password doesn't exist")
        except:
            print("User name or password doesn't exist")
    else:
        print("please enter somthing")
def home(option=None):
    option=input("login | signup :")
    if option == "login":
        access()
    elif option =="signup":
        register() 
    else:
        print("please enter an option")
home()
            
        
       
        