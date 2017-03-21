class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance+=amount
        
    def withdraw(self,amount):
        pass
        
    def displayBalance(self):
        pass
        
class CurrentAccount(BankAccount):
    def __init__(self,owner,balance,fee,limit):
        BankAccount.__init__(self, owner,balance)
        self.fee = fee
        self.limit = limit
    
    def displayBalance(self):
        print(self.balance)
    

Eoghan = CurrentAccount("Eoghan",1000,100,1000)

 

class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,rate,freq):
        BankAccount.__init__(self, owner, balance)
        self.interestRate = rate
        self.interestFrequency = freq
        
    def computeInterest(self):
        self.balance+=self.interestRate*self.interestFrequency
        
    def displayBalance(self):
        print(self.balance)
        
    def withdraw(self, amount):
        pass
        
class LumpSumAccount(SavingsAccount):
    def __init__(self, owner, balance, rate, freq, term,tf):
        SavingsAccount.__init__(self, owner, balance, rate, freq)
        self.savingsTerm = term
        self.withdrawalsAllowed = tf
        
    def withdraw(self, amount):
        self.balance -= amount
        
class RegularSaverAccount(SavingsAccount):
    def __init__(self, owner, balance, rate, freq, mindep, maxdep):
        SavingsAccount.__init__(self, owner, balance, rate, freq)
        self.monthlyMinimumDeposit = mindep
        self.monthlyMaximumDeposit = maxdep
    
    def checkDeposits(self):
        pass
        
    def applyDepositsPenalty(self):
        print(SavingsAccount.computeInterest(self)+SavingsAccount.balance)
    
    def withdraw(self, amount):
        BankAccount.withdraw(self, amount)
        self.balance-amount
    
Jake = LumpSumAccount("Jake",2000,0.2,0.2,2,True)

Jake.computeInterest()
Jake.displayBalance()

Dan = RegularSaverAccount("Dan",10000,0.1,5,100,1000)
Dan.displayBalance()
Dan.deposit(500)
Dan.displayBalance()
        