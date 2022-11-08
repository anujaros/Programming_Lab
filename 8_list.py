# list positive of positive integers
a = input("enter the numbers")
a = a.split()   #a = list(map(int,a))
pl=list()
a = [ int(x) for x in a]
for i in a:
    if i>0:
        pl.append(i)
print("positive integers:",pl)    


#square of N numbers
b=[x*x for x in a]
print ("The square of given numbers are:",b)

#list of vowels
v = input("enter a letter")
vo = [ "a", "e", "i","o", "u", "A", "E","I","O","U"]
a =[ x for x in v if x in vo]
print(a)

#list of ordinal value
ch = input("enter a letter")
ch = [ ord(x) for x in ch]
print(ch)



