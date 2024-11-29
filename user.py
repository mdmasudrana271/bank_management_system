from datetime import datetime
from transaction import Transaction

class User:
    def __init__(self,name,email,address,phone,account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.account_type = account_type
        self.bank =  None
        self.account = None
        self.transaction = []

    def deposit(self,amount):
        if self.account.status == True:
            curr_balance = self.account.balance
            self.account.balance +=amount
            self.bank.balance +=amount
            trans = Transaction("deposit",datetime.now(),self.account.account_no,amount,curr_balance,self.account.balance)
            self.transaction.append(trans)
            print(f"\n{amount} Taka is deposited on your account {self.account.account_no}\n")
        else:
            print(f"\nYour account is banned you can't deposit fund on this account!\n")
    
    def withdraw(self,amount):
        flag = self.bank.check_withdraw(self,amount)
        if flag:
            curr_balance = self.account.balance
            self.account.balance -=amount
            self.bank.balance -=amount
            trans = Transaction("withdraw",datetime.now(),self.account.account_no,amount,curr_balance,self.account.balance)
            self.transaction.append(trans)
            print(f"\nyour funds withdraw successfull withdraw amount is {amount} current balance is:{self.account.balance}\n")
        else:
            print("\nThe bank is bankkrupt or your withdraw amount is exceeded unsuccessful transaction!\n")

    
    def transfer(self,other_ac,amount):
        flag = self.bank.transfer(self,other_ac,amount)
        if flag:
            trans = Transaction("transfer",datetime.now(),self.account.account_no,amount,self.account.balance,self.account.balance-amount)
            self.transaction.append(trans)
    
    def req_loan(self,amount):
        flag = self.bank.req_loan(self,amount)
        if flag:
            curr_balance = self.account.balance
            self.account.balance +=amount
            self.bank.balance -=amount
            self.account.loan +=amount
            self.bank.loan +=amount
            trans = Transaction("loan",datetime.now(),self.account.account_no,amount,curr_balance,self.account.balance)
            self.transaction.append(trans)
            print(f"\nYour loan request has been approved {amount} is added to your account your current balance is {self.account.balance}\n")
    @property
    def check_balance(self):
        print(f"\nYour current balance is: {self.account.balance}\n")
    
    @property
    def loan_due(self):
        return self.account.loan
    

    def account_details(self):
        print(f"-----Account Details-----\nAccount No : {self.account.account_no }\nName : {self.name}\nEmail : {self.email}\nAddress : {self.address}\nPhone : {self.phone}\nCurrent Balance : {self.account.balance}\nLoan Balance : {self.account.loan}\nLoan_time : {self.account.loan_time}\nActiveity : {self.account.status}\n")
    

    def trans_history(self):
        if not self.transaction:
            print("\nTransaction history is empty\n")
        else:
            for trans in self.transaction:
                if trans.ac == self.account.account_no:
                    print(f"Transaction Type: '{trans.tran_type}'\tAmount: {trans.amount}\tTime: {trans.date.strftime('%I:%M:%S') }")
