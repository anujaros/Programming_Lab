#prompt user for list of integers- store 'over' for values above 100
li = input("Enter a list of integers:").split()
li =[int(x) for x in li]
L = len(li)

for e in range(L):
    if li[e] > 100:
        li[e] = 'over'

print(li)
