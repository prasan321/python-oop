class Person:
    #methods
    #Prefix all the instance variables with 'self'
    def __init__(self,name,age):
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

#create person object, #call __init method__ to set the person details
p1 = Person('Prasan', 33)
p1.greet()
p1.old()

#person 2
p2 = Person('Mike', 30)
p2.greet()
p2.old()

#New person 3
p3 = Person('Nike', 27)
p3.greet()
p3.old()