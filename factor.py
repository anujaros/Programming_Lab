def factor(n):
    lst=[]
    for j in range(1,n):
        if n % j == 0:
            lst.append(j)
    print("the factors of",n,"are:")
    print(lst)
            
    
factor(99)
