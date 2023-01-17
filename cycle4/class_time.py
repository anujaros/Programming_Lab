class Time:
    def __init__(self,h,m,s):
        self.sec= s%60
        self.min = (m +s//60)
        self.hr = (h + m//60 +s//3600)

    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
    
    def __add__(self,other):
        return Time(self.hr + other.hr, self.min +other.min, self.sec + other.sec)

t1 = Time(10,40,20)
t2 = Time(1,20,10)
t3 =t1+t2
print(t3)