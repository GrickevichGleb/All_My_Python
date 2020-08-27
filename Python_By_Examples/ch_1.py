
#name = input("Enter your name: ")
#print("Hello ", name)
#

##first_name = input("What is your first name: ")
##second_name = input("And a second name: ")
##print("Hello ", first_name, " ", second_name, "!")


#print("What do you call a bear with no teeth?\nA gummy bear")

##number1 = int(input("Enter first number: "))
##number2 = int(input("Enter second number: "))
##number3 = int(input("Enter third number: "))
##
##print("The answer is: ", (number1+number2)*number3)

##
##slices_start = int(input("How many slices you started with?: "))
##slices_eaten = int(input("How many have you eaten?: "))
##
##print("You have left with: ", slices_start - slices_eaten, ' slices')


##age = int(input("What is your age?: "))
##print("Next you will be: ", age+1)


##bill = float(input("Enter a bill price: "))
##diners_num = int(input("Enter how many diners where there: "))
###     formated output for floating point
###     '{:06.2f}'.format(3.141592653589793)  means we want output have at least 6 caracters
###     with 2 after decimal point 
##print("Each diner should pay: {:.4f}".format(bill/diners_num))


##num_of_days = int(input("Enter number of days: "))
##hours_in = num_of_days * 24
##minutes_in = hours_in * 60
##seconds_in = minutes_in * 60
##print("In ", num_of_days, 'is ', hours_in, ' hours, ', minutes_in, ' minutes, ', 'and ', seconds_in, ' seconds')
##


##kilos = float(input("Enter weigh in kilos: "))
##pounds = kilos*2.204
###            in formated string order of data set explicitly (first number in {} stands for variable in .format() )
##print("There are {1:.3f} pounds in {0:4.3f} kilos".format(kilos, pounds))


over_100 = int(input("Enter number over 100: "))
under_10 = int(input("Enter number under 10: "))
print("Smaler number goes in larger {} times".format(over_100//under_10))
