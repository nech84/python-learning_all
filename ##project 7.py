##project 7
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance  = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} successfully")
        print(f"New balance : {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdraw {amount} successfully")
        

    def check_balace(self):
        print(f"Owner {self.owner}")
        print(f"Balance {self.balance}")

acc = BankAccount("Alice",1000)
acc.deposit(500)
acc.withdraw(555)
acc.check_balace()
