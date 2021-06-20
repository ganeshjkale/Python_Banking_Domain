#!/usr/bin/python3
from customer_class import customer
from saving_account_class import saving_account


#Create a class that runs the program and accepts input from the end user to create respective class
#objects and print details. Add a method to perform deposit and withdrawal transaction based on the
#end user input.

class check_details():
    check_user_input=0
    def show_ask(self):
        print("\nEnter Number to select below :\n \
        \t 1 (Tip : Get User Account Details) \n \
        \t 2 (Tip : Deposit Money in Account) \n \
        \t 3 (Tip : Withdraw Money from Account) \n \
        \t 4 (Tip : Exit Program)")
         
    def __init__(self):
        try:
            #(ID,Initial Balance,Minimum Balance)
            self.saving_acc_obj = saving_account(123456789,1000,200)
            #self.show_ask()
            #self.check_user_input = int(input("Enter Number : " ))
        
            #if self.check_user_input == 1:
            cid = int(input("Enter Customer ID : " ))
            cname = input("Enter Customer Name : " )
            caddr = input("Enter Customer Address : " )
            ccont = int(input("Enter Customer Contact Details : " ))
            #Create customer object and initialized with above details (validation is remain on above data)     
            self.cust_obj = customer()
            self.cust_obj.add_customer_details(cid,cname,caddr,ccont)
       
            while True:
                self.show_ask()
                self.check_user_input = int(input("Enter Number : " ))
                if self.check_user_input == 1:
                    self.saving_acc_obj.getSavingAccountInfo()
                elif self.check_user_input == 2:
                    self.dep_amt = int(input("Enter Amount to Deposit : " ))
                    #self.saving_acc_obj.deposit(self.dep_amt)
                    self.user_deposit(self.saving_acc_obj,self.dep_amt)   
                elif self.check_user_input == 3:
                    self.with_amt = int(input("Enter Amount to Widthraw : " ))
                    #self.saving_acc_obj.widthraw(self.with_amt)
                    self.user_widthraw(self.saving_acc_obj,self.with_amt)
                elif self.check_user_input == 4:
                    break
                else:
                    print("Invalid Entry")                       
        except Exception as e:
            print(e)
    
    def user_widthraw(self,save_obj,with_amt=0):
        save_obj.widthraw(with_amt)
        
    def user_deposit(self,save_obj,dep_amt=0):
        save_obj.deposit(dep_amt)
        
        
    

u_obj = check_details()
    
    