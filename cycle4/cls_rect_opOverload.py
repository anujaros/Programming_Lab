class Rectangle:

    def __init__(self,l,w):
        self._length = l
        self._width = w
        

    def area(self):
        return self._length *self._width

    def __lt__(self,other):
        if self.area() < other.area():
            return True
        else:
            return False


r1 = Rectangle(int(input("enter the length:")),int(input("enter the width:")))

r2 = Rectangle(int(input("enter the length:")),int(input("enter the width:")))
               
if r1.area() < r2.area():
    print("area of second rectangle is greater")
else:
   print("Area of first rectangle is greater")



        
