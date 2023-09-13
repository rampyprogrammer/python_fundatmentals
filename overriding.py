class Bank_account:
    def __init__(self,AccoutNo,balance):
        self.__AccoutNo =AccoutNo
        self.__balance=balance

    def deposite(self,Amount):
        self.__balance += Amount

    def withdraw(self,Amount):
        if self.__balance >= Amount:
            self.__balance -= Amount

    def get_balance(self):
        return self.__balance
    
acount = Bank_account('AR1423535735',1000)

acount.deposite(500)
print(acount.get_balance())

acount.withdraw(400)
print(acount.get_balance())
