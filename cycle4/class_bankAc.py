class Bank_Account:
    
    def __init__(self ,name, ac_no, ac_type):
        self.name = name
        self.account_number = ac_no
        self.account_type = ac_type
        self.balance = 0
        
    def deposit(self):
        dep = float(input("enter the amount to be deposited: "))
        self.balance += dep
        self.balance()
        
    def withdraw(self):
        wth = float(input("enter the amount to be withdrawn: "))
        self.balance -= wth
        self.balance()
        
    def balance(self):
        if self.balance == 0:
            print(" no balance ")
        else:
            print(self.balance)



name = input("enter your name: ")
ac_no = int(input("enter your account number: "))
ac_type = input("enter your account type: ")

b1 = Bank_Account(name,ac_no,ac_type)

while(True):
    c = int(input(" 1 for deposit \n 2 for withdraw :"))

    if c==1:
        b1.deposit()
    elif c==2:
        b1.withdraw()
    else:
        print("wrong choice")
    
                    
                    
                    
