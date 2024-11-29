
class Transaction:
    def __init__(self,tran_type,date,ac,amount,curr_balance,aft_balance) -> None:
        self.tran_type = tran_type
        self.amount = amount
        self.date = date
        self.ac = ac
        self.curr_balance = curr_balance
        self.aft_balance = aft_balance

