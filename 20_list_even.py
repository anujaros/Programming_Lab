#list with even numbers removed
li = input("Enter any integers:")
li = li.split()
li = [int(x) for x in li]
new_l= []
for i in li:
    if i%2 != 0:
        new_l.append(i)
print("list with odd no:",new_l)        
