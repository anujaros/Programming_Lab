class Bank_Account:
    
    def __init__(self ,name, ac_no, ac_type):
        self.name = name
        self.account_number = ac_no
        self.account_type = ac_type
        self.balance = 0
        
    def deposit(self):
        dep = float(input("enter the amount to be deposited: "))
        self.balance += dep
    
        
    def withdraw(self):
        wth = float(input("enter the amount to be withdrawn: "))
        if wth > self.balance:
            print("Not available Balance\n")
        else:
            self.balance -= wth
            
        
    def Balance(self):
        print(self.balance)
    
        



name = input("enter your name: ")
ac_no = int(input("enter your account number: "))
ac_type = input("enter your account type: ")

b1 = Bank_Account(name,ac_no,ac_type)

while(True):
    c = int(input("1.Deposit \n2.Withdraw \n3.Balance\n4.Exit\nEnter your choice:\n"))

    if c==1:
        b1.deposit()
        
    elif c==2:
        b1.withdraw()
        
    elif c==3:
        b1.Balance()
        
    elif c==4:
        break
    else:
        print("wrong choice")

    
                    
                    
                    
