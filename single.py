class bank:
    def __init__(self):
        self.bank_name='ICICI'
        self.IFSC_code='134icici3567'
    
    
class acc_holder(bank):
    def __init__(self,name,acc_bal,acc_num):
        super().__init__()
        self.name=name
        self.acc_bal=acc_bal
        self.acc_num=acc_num
    def pri(self):
        print(f"""
              bank name  :  {self.bank_name}
              ifsc code  :  {self.IFSC_code}
              name of holder : {self.name}
              acc balance  : {self.acc_bal}
              acc num  :  {self.acc_num}""")
obj=acc_holder("rama",'10000000008rs','34145256783876809')
obj.pri()
