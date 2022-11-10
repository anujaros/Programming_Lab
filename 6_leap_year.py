#future leap year from current year to a final year
r= list()
yr1 = int(input("enter a year:"))
yr2= int(input("enter any year in the future:"))
for i in range(yr1,yr2+1):
	if i%4==0 and i%100== 0 and i%400==0:
	    r.append(i)
	elif i%4 ==0  and i%100 !=0:
	    r.append(i)
	else:
	    continue

print ("The leap years are:",r) #list of leap year
