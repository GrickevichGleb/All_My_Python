
##file = open("numbers.txt", 'w')
##file.write("1,2,3,4,5")
##file.close()


##file = open("Names.txt", "w")
##file.write("Name_1\n")
##file.write("Name_2\n")
##file.write("Name_3\n")
##file.write("Name_4\n")
###     print("text", file = file_name) can be use as an alternative to file.write
###     print("Name_3",file = file)
###     print("Name_4", file = file, end = "")
##file.close()


names = []
file = open("Names.txt", "r")
#print(file.read())
for line in file:
    print(line.strip())
    names.append(line.strip())
inp = input("Type one of the names: ")
file2 = open("Names2.txt", "w")
for name in names:
    if name != inp:
        file2.write(name+"\n")
file.close()
file2.close()
#--------------------------------------
file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt", "r")
selected_name = input("Enter a neame from the list: ")
selected_name = selected_name + "\n"
for row in file:
    if row != selected_name:
        file2 = open("Names2.txt", "a")
        newrecord = row
        file2.write(newrecord)
        file2.close
file.close


##file = open("Names.txt", "r")
##print(file.read())
##file.close()


##with open("Names.txt", "a") as file:
##    inp = input("Enter a name to add: ")
##    file.write(inp+"\n")
###    print(inp, file = file)   
##
##file = open("Names.txt", "r")
##print(file.read())
##file.close()




##again = True
##while again == True:
##    inp = int(input("""    1) Create a new file
##    2) Display the file
##    3) Add a new item to the file
##    Make a selection 1, 2 or 3
##    And 4 to exit: """))
##
##    if inp == 1:
##        file = open("Subject.txt", "w")
##        file.close()
##    elif inp == 2:
##        file = open("Subject.txt", "r")
##        print(file.read())
##        file.close()
##    elif inp == 3:
##        n = input("Enter a new subject to add: ")
##        file = open("Subject.txt", "a")
##        file.write(n+"\n")
##        file.close()
##    elif inp == 4:
##        again = False
##    else:
##        print("Error")
