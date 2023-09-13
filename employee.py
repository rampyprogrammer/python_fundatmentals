class employee:
    def __init__(self,name,sal,ext_amt,no_of_ot):
        self.name=name
        self.sal=sal
        self.ext_amt=ext_amt
        self.no_of_ot=no_of_ot
    def total_sal(self):
        return self.sal+(self.no_of_ot*self.ext_amt)
    

