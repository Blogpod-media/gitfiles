import datetime
import time

def calculate(a):
    return a


data = set()
class Bank:
    amount = 0
    def __init__(self):
        self.Bank_name = "State Bank of India"
        self.ifsc = 'SBI0N00012'
    
    def __repr__(self):
        return f'Bank Name: {self.Bank_name}, IFSC_Code : {self.ifsc} '

        # self.stored = datetime.date.today()

class CustomerDetails(Bank):
    check_amt = 18
    def __init__(self,name,identity,acc,op_amount):
        Bank.__init__(self)
        self.name = name
        self.identity = identity
        self.acc = acc
        self.op_amount = op_amount
        Bank.amount += self.op_amount
        self.count = 0

    def __repr__(self):
        return f'Name : {self.name}, Aaddhar_card : {self.identity}, Account No : {self.acc}, Amount : {self.op_amount}, Bank_Amount : {Bank.amount} '

    # stored = datetime.datetime.today()
    # def __repr__(self)
    def deposite(self,credit):
        self.credit = credit
        self.op_amount += self.credit
        Bank.amount += self.op_amount
        print(f'You\'ve added {self.credit} : Total Amount = {self.op_amount}')
        return (Bank.amount)
    
    def check_balance(self):
        self.count += 1
        if self.count > 3:
            self.op_amount -= CustomerDetails.check_amt
            return f'{self.name} due to over checking {CustomerDetails.check_amt} Rs. has been deducted. your Balance : {self.op_amount} '
        else:
            return f'{self.name} your Balance : {self.op_amount}'
            
    

# cus1 = CustomerDetails('Lucky','755376288106','67001010115773',5000)
# print(cus1)
cus2 = CustomerDetails('Pawan','755376288078','37376989161',10000)
print(cus2)
cus2.deposite(20000)
print(cus2.check_balance())
print(cus2.check_balance())
print(cus2.check_balance())
print(cus2.check_balance())
print(cus2)
# print(cus2.check_balance())


 print("Few changes are left to made so that it can help to replicate the Algorithm.")
