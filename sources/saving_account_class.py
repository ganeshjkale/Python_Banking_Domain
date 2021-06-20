#!/usr/bin/python3
from account_class import account

#Inherited class user super


class saving_account(account): 
    #Validate MinBalance before allowing withdrawals.
    SMinBalance=0
    
    def __init__(self,acc_id=0,acc_bal=0,min_bal=0):
        saving_account.SMinBalance = min_bal
        super().__init__(acc_id,acc_bal)
        #super(account,self).__init__(acc_id, acc_bal)
    
    def getSavingAccountInfo(self):
        try:
            print("=====================getSavingAccountInfo==================================")
            super().getAccountInfo()
            super().getBalance()
            print("Minimum Balance Required : " + str(saving_account.SMinBalance))
            print("===========================================================================")
        except Exception as e:
            print(e)
            
    def deposit(self,amt=0):
        super().deposit(amt)
    
    def widthraw(self,w_amt=0):
        if w_amt < account.balance - saving_account.SMinBalance:
            super().widthraw(w_amt)
        else:
            print("Withdraw Failed Cannot Widthraw beyond Minimum Balance")
        
    def getBalance(self):
        print("Mnimum Balance: " + str(saving_account.SMinBalance))
        super(saving_account,self).getBalance()