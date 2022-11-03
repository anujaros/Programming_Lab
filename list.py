#list comprehension
a = input("enter the numbers")
a = a.split()
#a = list(map(int,a))

# list positive of positive integers
pl=list()
a = [ int(x) for x in a]
for i in a:
    if i>0:
        pl.append(i)
print("positive integers:",pl)    


#square of N numbers
b=[x*x for x in a]
print ("The square of given numbers are:",b)



