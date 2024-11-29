from user import User

class Admin:
    def __init__(self,bank) -> None:
        self.user = "Admin"
        self.password = "12345"
        self.bank = bank


    def create_account(self,name,email,address,phone,account_type):
        user = User(name,email,address,phone,account_type)
        self.bank.create_account(user)

    def remove_account(self,account_no):
        self.bank.remove_account(account_no)
    
    def ban_account(self,account_no):
        self.bank.ban_account(account_no)

    def view_users(self):
        self.bank.view_users()

    def check_balance(self,bank):
        return bank.check_balance

    def set_loan_status(self,flag):
        self.bank.loan_available = flag
    

    def check_loan_status(self):
        return self.bank.loan_status

