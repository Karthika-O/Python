class Bank:
    def __init__(self,num=0,name=None,type=None,bal=0):
        self.num=num
        self.name=name
        self.type=type
        self.bal=bal
    def display(self):
        print('Account No : ',self.num)
        print('Account Holders Name : ',self.name)
        print('Account Type : ',self.type)
        print('Avail. Bal : ',self.bal)
    def deposit(self,amt):
        self.bal+=amt
        print('Deposited Successfully \n Current Blance = ',self.bal)
    def withdraw(self,amt):
        if(self.bal>=amt):
            self.bal-=amt
            print('Successfully Withdrawed \n Current Balance = ',self.bal)
        else:
            print('Insufficient Balance ')
b1=Bank(162007008,'Anuja Kumar','Savings',10000)
b1.display()
print('____________________________________________')
b1.deposit(2000)
print('____________________________________________')
b1.withdraw(1000)
        
    
