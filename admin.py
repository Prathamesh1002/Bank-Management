from typing import Any


class admin:
    def __init__(self,AC_No,name,balance):
        self.AC_No=AC_No
        self.name=name
        self.balance=balance
    def getAC_No(self):
        return self.AC_No
    def setAC_No(self,AC_No):
        self.AC_No=AC_No
    def getname(self):
        return self.name
    def setname(self,name):
        self.name=name
    def getbalance(self):
        return self.balance
    def setbalance(self,balance):
        self.balance=balance
    def __str__(self):
        return str(self.AC_No)+","+self.name+","+str(self.balance)+"\n"

    

    
    
    
        


    
    
        

