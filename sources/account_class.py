#!/usr/bin/python3
from bank_class import bank
from customer_class import customer
#Inherited class user super


class account(bank):
    AccountID=0
    balance=0

    def __init__(self,acc_id=0,acc_bal=0):
        account.AccountID = acc_id
        account.balance = acc_bal
        self.IFSC_code = "ACC012345"
        self.bankname = "HDFI"
        self.branchname = "FC_ROAD"
        self.loc = "Pune"
        #super().__init__("ACC012345","HDFI","FC_ROAD_PUNE","PUNE")
        super().__init__(self.IFSC_code,self.bankname,self.branchname,self.loc)

        #super(bank,self).__init__()
        #super().__init__(IFSC_code="ACC012345",bankname="HDFI",branchname="FC_ROAD_PUNE",loc="PUNE")
        
    def getAccountInfo(self):
        #Cust Object of Customer
        self.get_bank_details()
        self.cust_obj = customer()
        self.cust_obj.get_cust_details()
        print("Account ID : " + str(account.AccountID))
        
    def deposit(self,bal=0):
        self.balance = account.balance
        self.balance += bal
        account.balance = self.balance
    
    def widthraw(self,widthraw=0):
        if account.balance > widthraw:
            self.balance = account.balance
            self.balance -= widthraw
            account.balance = self.balance
            print("Withdraw Successful")
            print("Account Balance : " + str(account.balance))
            print("Self Account Balance : " + str(self.balance))
        else:
            print("Widthraw Failed")
    
    def getBalance(self):
        print("Account Balance : " + str(self.balance))
        return self.balance
        