
##total = 0
##while total <= 50:
##    number = int(input("Enter the number to add: "))
##    total = total + number
##    print("The total is: ", total)


##number = int(input("Enter a number: "))
##while number <= 5:
##    number = int(input("Enter a number: "))
##print("The last number you entered was:", number)


##num1 = int(input("Enter a number: "))
##num2 = int(input("Enter another number: "))
##res = num1 + num2
##c = input("Whant to add another number?:(y/n) ")
##while c == 'y':
##    num3 = int(input("Enter your num: "))
##    res = res + num3
##    c = input("Whant to add another number?:(y/n) ")
##print(res)

#__________________________
##num1 = int(input("Enter a number: "))
##res = num1
##c = 'y'
##while c == 'y':
##    num2 = int(input("Enter another number: "))
##    res = res + num2
##    c = input("Do you want to add another number: (y/n) ")
##print("The total is ", res)




##count = 0
##q = 'y'
##while q == 'y':
##    name = input("Enter the name of somebody to invite: ")
##    print(name, "has been invited")
##    count = count + 1
##    q = input("Want to invite somebody else?: (y/n) ")
##print(count, "people have been invited")



##compnum = 50
##a = int(input("Enter a number: "))
##count = 1
##while a != compnum:
##    if a < compnum:
##        print("Too low")
##    else:
##        print("Too high")
##    count = count + 1
##    a = int(input("Enter a number: "))
##print("Well done, you took",count,"attempts")


##number = int(input("Enter a number between 10 and 20: "))
##while number < 10 or number > 20:
##    if number < 10:
##        print("Too low")
##    if number > 20:
##        print("Too high")
##    number = int(input("Enter a number between 10 and 20: "))
##print("Thank you")


##bottles = 10
##while bottles > 0:
##    print("There are",bottles,"hanging on the wall")
##    print(bottles,"green bottles hangin on the wall")
##    print("and if 1 green bottle should accidentally fall ")
##    bottles = bottles - 1
##    q = int(input("How many bottles will be hanging on the wall?"))
##    while q != bottles:
##        print("No, try again")
##        q = int(input("How many bottles will be hanging on the wall?"))
##    print("There will be", bottles,"bottles hanging on the wall")
##print("There are no bottles on the wall")
    


#_______________________
bottles = 5
while bottles > 0:
    print("There are",bottles,"hanging on the wall")
    print(bottles,"green bottles hangin on the wall")
    print("and if 1 green bottle should accidentally fall ")
    bottles = bottles - 1
    q = int(input("How many bottles will be hanging on the wall?: "))

    if q == bottles:
        print("There will be", bottles,"bottles hanging on the wall")
    else:
        while q != bottles:
            print("No, try again")
            q = int(input("How many bottles will be hanging on the wall?: "))   
print("There are no bottles on the wall")
    















