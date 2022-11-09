d1 = {}
n= int(input("enter no. of items in the dictionary"))
for i in range(n):
    key = input("enter key")
    value = input("enter value")
    d1[key] = value
    

d2 = {}
n= int(input("enter no.of items in the dictionary"))
for i in range(n):
    key = input("enter key")
    value = input("enter value")
    d2[key] = value

    
#merging by updating one of th
#d1.update(d2)
#print(d1)

# Merging
d3 ={**d1,**d2}

for k, v in d3.items():
    if k in d1 and k in d2:
        d3[k]= [v,d1[k]]
print(d3)        


                  
    

