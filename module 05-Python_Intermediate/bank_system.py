class Banck:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit (self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print("Please check the amount")

    def withdraw(self,amount):
        if amount <= 0:
            print("The amount must be greater than zero.")
        elif amount <= self.balance:
            self.balance = self.balance - amount
            print(f"New Balance: {self.balance}")
        else:
            print(f"Insufficient funds: {self.balance}")

    def show_balance (self):
        print(f"{self.owner} Balance Account: {self.balance}")

    def transfer (self, destination, amount):
        if destination is self:
            print("you can't transfer money to you")
            return
        if amount <= 0:
            print("The amount must be greater than zero.")
        elif amount <= self.balance:
            self.balance = self.balance - amount
            destination.deposit(amount)
            print(f"New Balance: {self.balance}")
        else:
            print(f"Insufficient funds: {self.balance}")
        
client_1 = Banck("Jefferson", 100)
client_2 = Banck("Alejandro", 200)

client_2.transfer(client_1,50)
client_1.show_balance()
client_2.show_balance()
