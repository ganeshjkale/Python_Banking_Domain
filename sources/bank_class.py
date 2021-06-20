#!/usr/bin/python3

class bank():
    
    IFSC_code=""
    bankname=""
    branchname=""
    loc=""
    
    def __init__(self,ifc_code="",bank="",branch="",location=""):
        self.IFSC_code = ifc_code
        self.bankname = bank
        self.branchname = branch
        self.loc = location
        self.set_var_bank()

    def set_var_bank(self):
        bank.IFSC_code = self.IFSC_code
        bank.bankname = self.bankname
        bank.branchname = self.branchname
        bank.loc = self.loc
    
    def get_bank_details(self):
        print("\nAdded Bank Details Are Below")
        print("Bank IFSC Code : " + str(bank.IFSC_code))
        print("Bank Name : " + str(bank.bankname))
        print("Bank Branch Name : " + str(bank.branchname))
        print("Bank Location : " + str(bank.loc))
        

        