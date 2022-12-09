def len_of_longest(words):
	return max([len(word) for word in words])

a=input("Enter A List of Words : ").split()
print(len_of_longest(a))

#def len_longest_word():
#	wrds=input("Enter the words:").split()
#	x=0
#	for w in wrds:
#		if len(w) > x:
#			x= len(w)
#	print(x)
#len_longest_word()
