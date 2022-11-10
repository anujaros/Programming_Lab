# occursnce of 'a' within list
fname = ['Anna','Sarah','Aideen','Zeph','Raya']
count = 0
fn = " ".join(fname).lower()
for i in fn:
    if 'a' in i:
        count+=1
print("No. of occurence of a:",count)
