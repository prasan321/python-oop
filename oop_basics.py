'''
Python OOP Concepts - Basics
'''

#basic class
class Animal:
    pass

print(type(Animal))

class Person:
    #methods
    #Prefix all the instance variables with 'self'
    def set_details(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print('I am', self.name + '\n')
    
    def greet(self):
        if self.age < 80:
            print('Hello, how are you doing?')
        else:
            print('Hello, how do you do?')
        self.display()
    
    def old(self, ageing = 50):
        self.ageing = ageing
        self.age += self.ageing
        print('I am', self.age)

#create person object
p1 = Person()
#call set_details method to set the person details
p1.set_details('Prasan', 33)
#call greet function
p1.greet()
p1.old()

#person 2
p2 = Person()
p2.set_details('Mike', 30)
p2.greet()
p2.old()

#New person 3
p3 = Person()
p3.set_details('Nike', 27)
p3.greet()
p3.old()