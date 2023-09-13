def register():
    db =open("database.txt","r")
    print("""
          -:  instagram :-""")
    userName =input("creat your user name: ")
    password =input("creat password  :  ")
    confirm_password=input("enter the password again :  ")
    
    f=[]
    d=[]
    for i in db:
        a,b=i.split(", ")
        b=b.strip()
        f.append(a)
        d.append(b)
    data=dict(zip(f,d))
    print(data)
    
    
    if password == confirm_password:
        if len(password)<=6:
            print("password should contain atleast 8 charectors ")
            register()
        elif (password and userName) in d:
            print("account is already exist...")
            register()
        else:
            db=open("database.txt","a")
            db.write(userName+", "+password+"\n")
            print("account succesfully created")



def access():
    db=open("database.txt",'r')
    userName=input("enter username : ")
    password=input("enter password : ")
    
    if not len(password or userName)<1:
        f=[]
        d=[]
        for i in db:
            a,b=i.split(", ")
            b=b.strip()
            f.append(a)
            d.append(b)
        data=dict(zip(f,d))
        
        if data[userName]:
            if password==data[userName]:
                print("login successfull ")
                print("hi, ",userName)
                
            else:
                print("incorrect password or username")
                access()
        print("incorrect paasword or username")
        access()
        
def home(option=None):
    
    option=input("login | signup :")
    if option == "login":
        access()
    elif option =="signup":
        register() 
    else:
        print("please enter an option")
home()
            
                
    
        