'''
How to set getters and setters
'''

class Product:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x,self._y)
    
    #Getter
    @property
    def value(self):
        return self._x
    #Setter
    @value.setter
    def value(self,val):
        self._x = val

p = Product(12,24)

print(p.value)
print(p.value + 2)

print(dir(Product))