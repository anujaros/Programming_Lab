

def fib(n):
    a,b=0,1
    while(n>=1):
        n-=1
        print(a)
        a,b=b,a+b

count = int(input("Enter a number"))
fib(count)
