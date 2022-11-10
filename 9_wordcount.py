#count occurance of each word in a line of text
d = dict()
txt =input("Enter a line of text:")
word = txt.lower().split()

for i in word:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)
