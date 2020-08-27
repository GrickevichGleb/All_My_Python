
##name = input("Enter your name: ")
##count = int(input("counter: "))
###     for i in range(1, 4)/ ...range(count)
##for i in range(count):
##    print(name)


##name = input("Enter your name: ")
##count = int(input("counter: "))
###     for i in range(count) but i isnt used, so can be omited
##for _ in range(count):
##    for c in name:
##        print(c)


##number = int(input("Enter a number beetwen 1 and 12: "))
##for i in range(1, 11):
##    print(i,'x',number,'=',i*number)


##number = int(input("Enter the num below 50: "))
##for i in range(50, number-1, -1):
##    print(i)


##name = input("Enter your name: ")
##num = int(input("Num of times: "))
##if num < 10:
##    for i in range(num):
##        print(name)
##else:
##    for i in range(1, 4):
##        print("Too high")


##total = 0
##for i in range(5):
##    num = int(input("Enter the num: "))
##    com = input("Add it to the total: ")
##    if com.lower() == 'yes':
##        total = total + num
####    elif com.lower() == 'no':
####        print("-|-")
##print('Total is: ', total)


##direction = input("Direction to count (up/down): ")
##if direction.lower() == 'up':
##    top_num = int(input("Enter the top number: "))
##    for i in range(1, top_num+1):
##        print(i)
##elif direction.lower() == 'down':
##    num = int(input("Enter the num below 20: "))
##    for i in range(20, num-1, -1):
##        print(i)
##else:
##    print("i don't understand")


number = int(input("How many people you want to invite: "))
if number < 10:
#   for i in range(number):
    for i in range(0, number):
        name = input("Enter the name: ")
        print(name,"has been invited")
else:
    print("Too many people")







