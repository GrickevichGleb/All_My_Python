
##name = input("Enter your name: ")
##print("Your name length: ",len(name))
##surname = input("Enter your surname: ")
##print("Your surname length: ", len(surname))
###      full_name = name + " " + surname
##full_name = " ".join([name, surname])
##print(full_name)
##print("Your full name length: ", len(full_name))


##subj = input("Entre your favourite school subject: ")
##for letter in subj:
##    print(letter, end="-")


##text_string = "This is a text line for example of useing string sections"
##print(text_string)
##start_p = int(input("Enter the start point: "))
##end_p = int(input("Enter the end point: "))
##print(text_string[start_p : end_p])


##user_inp = input("Enter a string in uppercase: ")
##while user_inp.isupper() == False:
##    print("Try again")
##    user_inp = input("Enter a string in uppercase: ")
##print("Well its in upper case")


##post_code = input("Enter your postcode: ")
##for i in post_code[0 : 2]:
##    print(i.upper(),end='')
    

##vowels = ["a", "e", "i", "o", "u"]
##name = input("Enter your name: ")
##count = 0
##for letter in name:
##    if letter in vowels:
##        count = count + 1
##print("There is",count,"vowels in your name")


##ent_pass = input("Enter your password: ")
##ent_pass2 = input("Repeat it: ")
##if ent_pass == ent_pass2:
##    print("Thank you")
##elif ent_pass.lower() == ent_pass2.lower():
##    print("They must be in the same casse")
##else:
##    print("Incorrect")


inp_word = input("Enter a word: ")
print(inp_word[-1])
#        from last index to (-1)-index(exclusively) with step -1
for l in range(len(inp_word)-1, -1, -1):
    print(inp_word[l])

#----------------------

##word = input("Enter a word: ")
##length = len(word)
##num = 1
##for x in word:
##    position = length - num
##    letter = word[position]
##    print(letter)
##    num = num + 1















