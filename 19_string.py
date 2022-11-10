#Exercise 19
#create single string separated with space from 2 strings by swapping the character at position 1
s1 =input("Enter a string_1:")
s2 = input("Enter a string_2:")

print(s2[0] + s1[1:] +" " + s1[0] + s2[1:])
