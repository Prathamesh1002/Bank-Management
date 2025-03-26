class bank:

    def __init__(self,AC_No,amount,Operation,date):
        self.AC_No=AC_No
        self.name=amount
        self.balance=Operation
        self.date=date

    def getAC_No(self):
        return self.AC_No
    def setAC_No(self,AC_No):
        self.AC_No=AC_No

    def amount(self):
        return self.amount
    def setamount(self,amount):
        self.amount=amount

    def Operation(self):
        return self.Operation
    def setOperation(self,Operation):
        self.Operation=Operation

    def date(self):
        return self.date
    def setdate(self,date):
        self.date=date
    def __str__(self):
        return str(self.AC_No)+","+str(self.amount)+","+self.Operation+","+str(self.date)+"\n"
    

    
    
    
        


    
    
        

