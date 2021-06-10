class Rectangle():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    #property  as a instantiate variable
    @property
    def diagnal(self):
        return (self.length*self.length + self.breadth*self.breadth)**0.5
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2*(self.length * self.breadth)

r = Rectangle(2,5)

print(r.diagnal) #property  as a instantiate variable
print(r.area()) #calling function
print(r.perimeter())