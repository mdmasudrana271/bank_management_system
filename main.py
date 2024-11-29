from bank import Bank
from user import User







bd_bank = Bank("Bangladesh Bank",10000000)

def admin_panel():
    print("\n-----Admin Panel-----\n")
    user_id = input("Enter your admin user ID: ")
    password = int(input("Enter you admin password: "))
    admin = bd_bank.req_admin(user_id,password)
    if admin is None:
        print("\nInvalid admin credential\n")
        return
    
    while True:
        print("\n1. Create an account")
        print("2. Remove an user account")
        print("3. View all users account")
        print("4. Check total available balance of the bank")
        print("5. Check total loan amount of the bank")
        print("6. Bann an user account")
        print("7. Set loan availability")
        print("8. Check loan status")
        print("9. Exit")

        choice = int(input("Enter your admin choice: "))

        if choice == 1:
            name = input("Enter your name: ")
            email = input("Enter your email address: ")
            address = input("Enter your address: ")
            phone = int(input("Enter your phone number: "))
            account_type = input("Enter your account type (Savings/Cuurent): ")
            admin.create_account(name,email,address,phone,account_type)
        elif choice == 2:
            account_no = int(input("Enter account number: "))
            admin.remove_account(account_no)
        elif choice == 3:
            admin.view_users()
        elif choice == 4:
            print(f"\nTotal available balance is: {admin.check_balance(bd_bank)}")
        elif choice == 5:
            print(f"\nTotal loan amount is: {bd_bank.loan}\n")
        elif choice == 6:
            account_no = int(input("Enter account number: "))
            admin.ban_account(account_no)
        elif choice == 7:
            flag = input("Set loan activity (True/False): ")
            admin.set_loan_status(flag)
        elif choice == 8:
            flag = admin.check_loan_status()
            if flag == True:
                print("\nLoan activity is enable\n")
            else:
                print("\nLoan activity is disabled\n")
            
        elif choice == 9:
            print("\nThank for visit!\n")
            break
        else:
            print("\nInvalid choice!\n")


def user_panel(user):
    print("\n-----User Panel-----\n")
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Request for loan")
        print("5. See transaction history")
        print("6. Account Details")
        print("7. Check balance")
        print("8. Check loan due amount")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter your deposit amount: "))
            user.deposit(amount)
        elif choice == 2:
            amount = int(input("Enter withdraw amount: "))
            user.withdraw(amount)
        elif choice == 3:
            account_no = int(input("Enter transfer account number: "))
            amount = int(input("Enter transfer amount: "))
            user.transfer(account_no,amount)
        elif choice == 4:
            amount = int(input("Enter loan amount: "))
            user.req_loan(amount)
        elif choice == 5:
            user.trans_history()
        elif choice == 6:
            user.account_details()
        elif choice == 7:
            user.check_balance
        elif choice == 8:
            print(f"\nYour current loan due balance is: {user.loan_due}\n")
        elif choice == 9:
            print("Thanks for visit")
            break
        else:
            print("Invalid choice")
    


def login(bank):
    ac = int(input("Enter your account number: "))
    for user in bank.users:
        if user.account.account_no == ac and user.account.status==True:
            print(f"-----Welcome Back {user.name}-----\n")
            return user_panel(user)
        else:
            print("Invalid credetials or your account is banned")
    

def signup(bank):
    print("\nWelcome to Bangladesh Bank Ltd...\n")
    print("\nEnter your credentials for create a new account\n")
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    address = input("Enter your address: ")
    phone = int(input("Enter your phone number: "))
    account_type = input("Enter your account type (Savings/Current): ")
    user = User(name,email,address,phone,account_type)
    bank.create_account(user)
    user_panel(user)


while True:
    print("Welcome to Bangladesh Bank Ltd...\n")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
       admin_panel()
    elif choice == 2:
        flag = input("Login/Sign up (L/S): ")
        if flag.lower()=="l":
            login(bd_bank)
        elif flag.lower()=="s":
            signup(bd_bank)
        else:
            print("\nInvalid input\n")
    elif choice == 3:
        print("\nThanks for visit our bank!\n")
    else:
        print("\nInvalid choice!\n")