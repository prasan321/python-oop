'''
Python OOP Concepts - Basics
'''

#basic class
class Animal:
    pass

print(type(Animal))

class Person:
    #methods
    def set_details(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print('I am', self.name)
    
    def greet(self):
        if self.age < 80:
            print('Hello, how are you doing?')
        else:
            print('Hello, how do you do?')
        self.display()

#create person object
p1 = Person()
p2 = Person()

#call set_details method to set the person details
p1.set_details('Prasan', 33)
p2.set_details('Mike', 30)

#call greet function
p1.greet()
p2.greet()