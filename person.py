'''
This Person class will be use as a module for another person class called client.py
'''
class Person:
    def __init__(self,name,age):
        self.name = name
        if 20 < age < 80:
            self._age = age
        else:
            raise ValueError('Age must be between 20 and 80 !!!')
    
    def display(self):
        print(self.name, self._age)
    
    def set_age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError('Age must be between 20 and 80 !!!')
    
    def get_age(self):
        return self._age

if __name__ == '__main__':
    p = Person('Prasan', 30)
    p.display()

    p.set_age(p.get_age() + 2)
    p.display()