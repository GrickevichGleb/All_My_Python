
##name = input("Enter your name: ")
##print(len(name))


##first_name = input("Enter your first name: ")
##second_name = input("Enter your second name: ")
##full_name = first_name + ' ' + second_name
###     full_name = ' '.join([first_name, second_name])
##print("Full name: ", full_name, " Length: ", len(full_name))


##first = input("Enter your first name in liwer case: ")
##sure = input("Enter your sure name in liwer case: ")
##first = first.title()
##sure = sure.title()
##full_name = first + ' ' + sure
##print(full_name)


##rhyme = input("Enter a rhyme: ")
##print(len(rhyme))
##st_ind = int(input("Starting number: "))
##en_ind = int(input("Ending number: "))
###     [x : y] - from x to y, x inclusively/y exclusively
##print(rhyme[st_ind : en_ind])


##word = input("Type any word: ")
###     Returns in upper case (variable 'word' remains the same)
##print(word.upper())


##first = input("Enter your first name: ")
##if len(first) < 5:
##    surename = input("Enter your surename: ")
##    fullname = first + surename
##    print(fullname.upper())
##else:
##    print(first.lower())


vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Enter a word: ')
#     first = word[o]
#     if first != 'a' and first != 'e' and first != 'i' and first != 'o' and first != 'u':
if word[0] not in vowels:
    word = word[1:] + word[0] + 'ay'
else:
    word = word + 'way'
print(word.lower())
