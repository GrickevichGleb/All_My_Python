#Generator examples


data = [1, 2, 3, 4, 5, 6, 7, 8]

#creates list of evens 
evens = [num for num in data if not num % 2]
print(evens)


#creates list of only strings (instance checks if 'num'(from for cycle) is of type 'str')
data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = [num for num in data if isinstance(num, str)]
print(words)


#Without generators
#data will contain separated words 
data = list('So long and thanks for all the fish'.split())
title = []
#title() applyes "Header Style" (Words Starts From Capital Letter)
for word in data:
	title.append(word.title())

#With generators
title2 = [word.title() for word in data]
print(title2)


#Using for to create set
vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Don't forget to pack your towel."

found = set()
for v in vowels:
        if v in message:
                found.add(v)

#Use of set generators
#To destinguish from dictionaries look at the ":" (there is no ":" in set generators only one value)
found2 = {v for v in vowels if v in message}
print(found2)
