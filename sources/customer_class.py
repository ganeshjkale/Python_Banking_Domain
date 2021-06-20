#!/usr/bin/python3

class customer():
    CustomerID=0
    custname=0
    address=0
    contactdetails=0
    
    def __init__(self):
        #print("\nNow in Customer class")
        pass
       
    def add_customer_details(self,cust_id=0,cust_name=0,cust_add=0,cust_contact=0): 
        customer.CustomerID = cust_id
        customer.custname = cust_name
        customer.address = cust_add
        customer.contactdetails = cust_contact
        self._print_details()
        
        
    def _print_details(self):
        print("\nAdded Customer Details Are Below")
        print("Customer ID : " + str(customer.CustomerID))
        print("Customer Name : " + customer.custname)
        print("Customer Address : " + customer.address)
        print("Customer Contact Details : " + str(customer.contactdetails ))   
            
    def get_cust_details(self):
        self._print_details()
            
        