import csv
import random

##file = open("Books.csv", 'w')
##header = "Book,Author,Year Released\n"
##file.write(str(header))
##book1 = "To Kill a Mockingbird,Harper Lee,1960\n"
##book2 = "A Brief History of Time,Stephen Hwaking,1988\n"
##book3 = "The Great Gatsby,F.Scott Fitzgerald,1922\n"
##book4 = "The Man Who Mistook His Wife for a Hat,Oliver Sacks,1985\n"
##book5 = "Pride and Prejudice,Jane Austein,1813\n"
##file.write(book1)
##file.write(book2)
##file.write(book3)
##file.write(book4)
##file.write(book5)
##file.close()


##file = open("Books.csv", "a")
##title = input("Enter a title: ")
##author = input("Enter author: ")
##year = input("Enter the year it was released: ")
##new_record = title + ',' + author + ',' + year + '\n'
##file.write(str(new_record))
##file.close()
##
##file = open("Books.csv", "r")
##ignore = file.readline()
##for row in file:
##    print(row)
##file.close()


##file = open("Books.csv", "a")
##count = int(input("How many records do you want to add: "))
##for i in range(count):
##    title = input("Enter a title: ")
##    author = input("Enter author: ")
##    year = input("Enter the year it was released: ")
##    record = title + ',' + author + ',' + year + '\n'
##    file.write(str(record))
##file.close()
##
##file = open("Books.csv", "r")
##search = input("Enter the author youra are searching for: ")
###reader = csv.reader(file)
##count = 0
##for row in file:
##    if search in str(row):
##        print(row)
##        count = count + 1
##if count == 0:
##    print("There are no books by that author in this list.")
##file.close()


##file = open("Books.csv", 'r')
##start_year = int(input("Enter a starting year: "))
##end_year = int(input("Enter an end year: "))
##book_list = list(csv.reader(file))
##
##for row in book_list[1:]:
##    if int(row[2]) >= start_year and int(row[2]) <= end_year:
##        print(row)
##file.close()
#---------------------------------------------
##start = int(input("Start year: "))
##end = int(input("End year: "))
##
##file = list(csv.reader(open("Books.csv")))
##tmp = []
###   should be file[1:] to skip first line that contain columns names
##for row in file[1:]:
##    tmp.append(row)
##
##x = 0
##for row in tmp:
##    if int(tmp[x][2]) >= start and int(tmp[x][2]) <= end:
##        print(tmp[x])
##    x = x + 1
    

##file = open("Books.csv", "r")
##x = 1
##for row in file:
##    print(x,"): ", end='')
##    print(row, end='')
##    x = x + 1


##file = list(csv.reader(open("Books.csv")))
##tmp = []
##header = ['Title', 'Author', 'Year\n']
##for row in file[1:]:
##    tmp.append(row)
##
##x = 0
##for row in tmp:
##    display = x, row
##    print(display)
##    x = x + 1
##
##delete = int(input("Which row would you remove?: "))
##del tmp[delete]
##
##x = 0
##for row in tmp:
##    display = x, row
##    print(display)
##    x = x + 1
##
##change_ind = int(input("Which row would you change?: "))
##x = 0
##for row in tmp[change_ind]:
##    display = x, tmp[change_ind][x]
##    x = x + 1
##
##part = int(input("Which part do you want to change?: "))
##new_data = input("Enter a new data: ")
##tmp[change_ind][part] = new_data
##print(tmp[change_ind])
##    
####new_data = []
####print("Input new: ")
####title = input("Title: ")
####author = input("Author: ")
####year = input("Year: ")
####new_data.append(title)
####new_data.append(author)
####new_data.append(year)
####print("New data: ", new_data)
####
####tmp[change_ind] = new_data
####tmp.insert(0,header)
##
##x = 0
##for row in tmp:
##    display = x, row
##    print(display)
##    x = x + 1 
##
##file = open("Books2.csv", 'w')
##for row in tmp:
##    new_rec = row[0] + ',' + row[1] + ',' + row[2] + '\n'
##    file.write(new_rec)
##file.close()



score = 0
name = input("Enter your name: ")
a = random.randint(0,10)
b = random.randint(0,10)
question1 = str(a) + " + " + str(b)
ans1 = int(input(question1 + ' = '))
if ans1 == (a+b):
    score = score + 1
a = random.randint(0,10)
b = random.randint(0,10)
question2 = str(a) + " + " + str(b)
ans2 = int(input(question2 + ' = '))
if ans2 == (a+b):
    score = score + 1

file = open("Quiz.csv", 'a')
data = name + ',' + question1 + ',' + str(ans1) + ',' + question2 + ',' + str(ans2) + ',' + str(score) + '\n'
file.write(str(data))
file.close()






