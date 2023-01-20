f1 = open("sample.txt","r")
f2 = open("odd.txt","r+")
fr = f1.read().splitlines()
for i in range(len(fr)):
	if i%2 ==0:
		f2.write((fr[i]+"\n"))


f1.close()
f2.close()

