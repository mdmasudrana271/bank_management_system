from account import Account
from admin import Admin

class Bank:
    ac_serial = 12340000
    def __init__(self,name,investment) -> None:
        self.name = name
        self.balance = investment
        self.users = []
        self.loan = 0
        self.loan_available = True



    @property
    def loan_status(self):
        return self.loan_available 
    
    @loan_status.setter
    def loan_status(self,clock):
        self.loan_available = clock

    @property
    def check_balance(self):
        return self.balance


    def ac_no_generate(self):
        self.ac_serial+=1
        return self.ac_serial
    
    def create_account(self,user):
        ac = Account(self.ac_no_generate())
        user.account = ac
        user.bank = self
        self.users.append(user)
        print("\nYour account has been created!\n")

    def remove_account(self,account_no):
        user = None
        for man in self.users:
            if man.account.account_no == account_no:
                user = man
                break

        if user is not None:
            self.users.remove(user)
            print(f"{account_no} is removed successfully!")
        else:
            print(f"{account_no} is not valid!")


    def ban_account(self,account_no):
        ac = None
        for user in self.users:
            if user.account.account_no == account_no:
                ac = user
                break
        if ac is not None:
            ac.account.status = False
            print(f"\n{account_no} is banned successfully!\n")
        else:
            print(f"\n{account_no} is not valid!\n")

    def view_users(self):
        print(f"\nTotal account is {len(self.users)}\n")
        for user in self.users:
            print(f"User_Name: {user.name}\tAccount No : {user.account.account_no}\tBalance:  {user.account.balance}")


    def req_admin(self,user,password):
        admin = None
        if user =="admin" and password == 12345:
            admin = Admin(self)

        return admin
    
    def check_withdraw(self,user,amount):
        if user.account.status == False:
            return None 
        elif user.account.balance - amount < 0:
            return False
        else :
            return True
    
    def transfer(self,user,other_ac,amount):
        person = None
        for man in self.users:
            if man.account.account_no == other_ac:
                person = man
                break
        if person is None:
            print(f"{other_ac} is not valid")
            return None
        elif user.account.status == False or person.account.status==False:
            print("\nUser account is banned you can't transfer fund\n")
            return None
        elif user.account.balance -amount<0:
            print("\nInsufficient balance to transfer")
        else:
            user.account.balance -= amount
            person.account.balance +=amount
            print(f"\nfund transfer is successfull transfer amount is: {amount} from {user.account.account_no} to {other_ac}!\n")
            return True

    def req_loan(self,user,amount):
        if self.loan_status == False or user.account.status == False or user.account.loan_time>1 or self.balance-amount<=0:
            return False
        else:
            return True


