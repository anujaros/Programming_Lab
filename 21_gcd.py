x =int(input("Enter a number:"))
y = int(input("Enter another number:"))
m = max(x,y)
for i in range(1,m):
    if x%i == 0 and y%i == 0:
        c=i

print("GCD of",x,'and',y,'are:',c)
