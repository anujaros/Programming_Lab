num = input("enter three numbers")
num = num.split()
num = [float(x) for x in num]
c = 0
for i in num:
    if i>c:
        c=i
print("The largest no. of the three is:",c)        
    
