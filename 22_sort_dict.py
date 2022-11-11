d = dict()
n= int(input("Enter no. of items in the dictionary:"))
for i in range(n):
    key = input("enter key: ")
    value = input("enter value: ")
    d[key] = value
    
print("Dictionary sorted interms of keys")
print("In ascending order:",dict(sorted(d.items())))
print("In descending order:",dict(sorted(d.items(), reverse=True)))

print("Dictionary sorted interms of values:")
print("In ascending order:",dict(sorted(d.items(), key = lambda item: item[1])))
print("In descending order:",dict(sorted(d.items(), key=lambda item:item[1],reverse=True)))
