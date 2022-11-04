l1 =input(" Enter the integers for the 1st list:")
l1 = list(map(int,l1.split()))
l2 =input("Enter the integers for the 2nd list:")
l2 =list(map(int,l2.split()))


#length

if len(l1) == len(l2):
    print("The lists are of same length")
else:
    print("The lists are of different length")

#lists sum to same value or not
if sum(l1) == sum(l2):
    print("The lists sum to same value")
else:
    print("The lists sum to different value")

# checking for common element

commn_elm = [s for s in l1 if s in l2]
if len(commn_elm) == 0:
    print("Common element doesn't exist")
else:
    print("Common element is present")


