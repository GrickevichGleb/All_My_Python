import math

##number = float(input("Enter a number with decimal places: "))
##number = number * 2
###     round(num, 2) rounds number to 2 decimal places
##print(round(number, 2))


##number = int(input("Enter an int over 500: "))
###     works out the square root (import math requid)
##root = math.sqrt(number)
##print(round(root, 2))


###     math.pi - π
##print(round(math.pi, 5))


##rad = float(input("Enter the radius of a circle: "))
###     area is: π*radius^2
##area = math.pi * rad**2
##print(area)


##rad = float(input("Enter the radius of a circle: "))
##depth = float(input("Enter the depth of cylinder: "))
##area = math.pi * (rad**2)
##volume = area * depth
##print(round(volume, 3))


##num1 = int(input("Enter the num1: "))
##num2 = int(input("Enter the num2: "))
###     whole number division (//)
##whole = num1 // num2
##remainder = num1 % num2
##print(num1,'divided by',num2,'is',whole,'with',remainder,'remaining')


inp = int(input("1) Square\n2) Triangle\n\nEnter a number: "))
if inp == 1:
    side_len = float(input("Enter the side length: "))
#     res = side_len * side_len
    res = side_len**2
    print("The area is: ", res)
elif inp == 2:
    base = float(input("Enter the base len of triangle: "))
    height = float(input("Enter the height of triangle: "))
    res = (base * height) / 2
    print("The area is: ", res)
else:
    print("Some error occured!")



    




