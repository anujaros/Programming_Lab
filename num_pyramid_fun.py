def py(n):
	for i in range(1,n+1):
		for j in range(1,i+1):
			print(j*i,end=" ")
		print()
			
n = int(input("enter num:"))
py(n)