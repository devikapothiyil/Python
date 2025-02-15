class Account:
    def __init__(self,bal,accnt_no):
        self.bal=bal
        self.accnt_no=accnt_no

    def debit(self,amount):
        self.bal-=amount
        print(" Rs.",amount,"Debited Succesfully..")

    def credit(self,amount):
        self.bal+=amount
        print(" Rs.",amount,"credited Succesfully..")

    def balance(self):
        print("Balance of",self.accnt_no," is ",self.bal)

a1=Account(25000,2345)
a1.debit(40)
a1.credit(20)
a1.balance()