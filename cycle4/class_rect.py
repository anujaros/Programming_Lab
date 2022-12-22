class Rectangle:
    
    def __init__(self):
        l,b = [ int(x) for x in input("enter the no.").split() ]
        self.length = l
        self.breadth = b
        
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def area(self):
        return (self.length * self.breadth)

def comp():
    a1 =r1.area()
    a2 = r2.area()
    if a1<a2:
        print("area of second rectangle is greater")
    else:
        print("area of first rectangle is greater")
r1 = Rectangle()

r2 = Rectangle()

comp()
