'''
Practice Exercise -1
Make a class that represents a bank account. Create four methods named set_details, display, withdraw and deposit.
In the set_details method, create two instance variables : name and balance. The default value for balance should be zero. In the display method, display the values of these two instance variables.
Both the methods withdraw and deposit have amount as parameter. Inside withdraw, subtract the amount from balance and inside deposit, add the amount to the balance.
Create two instances of this class and call the methods on those instances.
'''

class BankAccount():
    def set_details(self,name,balance=0):
        self.name = name
        self.balance = balance
        
    def display(self):
        print('My name and accont balance:',self.name, self.balance)

    def withdraw(self,amount):
        self.amount = amount
        self.balance = self.balance - self.amount
        print('My account balance =', self.balance)

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print('My account balance =', self.balance)

b = BankAccount()

b.set_details('Prasan', 1000)

b.display()

b.withdraw(100)

b.deposit(200)