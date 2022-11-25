def pattern(n):
    for  i in range(n+1):
        print(i*"*")
        if i== n:
            for e in range(n-1, 0,-1):
                print(e*"*")



pattern(5)
            
