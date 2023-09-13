class insta_book:
     def __init__(self):
         self.user=input("""
         insta       book  
     creat account(c)  or login(l): """).upper()
         if self.user in ["C","L"]:
             match self.user:
                 case "C": self.creat_account()
                 case "L": self.login()
     def creat_account(self):
        print(""" 
              instabook
     -: creat your account :-""")
        self.name=input("name     : ")
        self.email=input("email   :")
        self.phone =int(input("phone num     :  "))
        self.password1=input("password   :   ")
        self.confirm_password=input("confirmpassword   :   ")
        
        
        if self.password1==self.confirm_password:
            file=open("data.txt","a")
            file.write(f"Name :{self.name},email :{self.email},phone :{self.phone},password  :{self.password1},confirm password :{self.confirm_password}")
            file.close()
            
     def login(self):
         self.phone=int("phone   :   ")
         self.password=input("password  :   ")
         if self.phone and self.password:
             file=open("data.txt","r")
             
             l2=[i.split(",") for i in file.readlines()]
             
             
         
    