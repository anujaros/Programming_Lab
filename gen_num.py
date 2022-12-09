def perfect_sqr(n):
    if int(n**0.5) == n**0.5:
        return True
def even(n):
    sn =str(n) ; q=''
    for e in sn:
        if int(e)%2 ==0:
            q+= e
    if len(q)==len(sn):
        return True

x = int(input("Enter the lower limit:"))
y = int(input("Enter the upper limit:"))
if len(str(x))== len(str(y)) == 4:
    for i in range(x,y+1):
        if perfect_sqr(i)== True and even(i)== True:
            print(i)
else:
    print("Invalid Entry; Inputs must be 4 Digit No.")
