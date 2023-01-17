class publisher:
    def __init__(self,n):
        self.name = n

class book(publisher):
    def __init__(self,n,t,a):
        publisher.__init__(self,n)    
        self.title = t
        self.author = a

    def display(self):
        print("Title :".self.title,"\nAuthor :",self.author)

class python(book):
    def __init__(self, n, t, a,p,pg):
        book.__init__(self,n,t,a)
        self.price = p
        self.pgn =pg
    def display(self):
        print("Name :",self.name,"\nTitle :",self.title,"\nAuthor :",self.author,"\nPrice :",self.price,"\nNo. of pages :",self.pgn)    
        

obj= python("Lakshmi Rao Publications","Python Programming","Lakshmi Rao",1200,900)
obj.display()