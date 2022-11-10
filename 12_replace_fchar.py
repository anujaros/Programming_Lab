# create string with first character replaced with $ except first character
wrd = input("Enter a word:").lower()
lst =[]
for e in wrd:
    lst.append(e)
l=len(lst)
for i in range(1,l):
    if lst[0] in lst[i]:
        lst[i]= '$'
print("".join(lst))


#s = input("Enter the string : ")
#new = s[1:].replace(s[0], '$')
#print(s[0]+new)
        
