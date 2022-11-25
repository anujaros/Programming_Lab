def str_end(a= input("Enter a string:")):
    if a[-3:] == "ing":
        new = a[:-3] + "ly"
    else:
        new = a + "ing"
    print( new)
str_end()
