from array import *
import random
import math


##ints = array('i',[])
##for i in range(0,5):
##    user_inp = int(input("Enter integer: "))
##    ints.append(user_inp)
##ints = sorted(ints)
##ints.reverse()
##print(ints)


##nums = array('i',[])
##for num in range(0, 5):
##    i = random.randint(0,10)
##    nums.append(i)
##for x in nums:
##    print(x)


##nums = array('i', [])
##while len(nums)<5:
##    n = int(input("Enter the num between 10 and 20: "))
##    if n > 10 and n < 20:
##        nums.append(n)
##        print(len(nums))
##    else:
##        print("Outside the range")
##        
##print("Thank you")
##for x in nums:
##    print(x)


##nums = array('i', [2,2,1,4,4,4,5,0])
##print(nums)
##user_inp = int(input("Enter some num from array: "))
##count = nums.count(user_inp)
##print(user_inp,"appears",count,"times in the array")


##ar1 = array('i',[])
##inp1 = int(input("Enter a num1: "))
##inp2 = int(input("Enter a num2: "))
##inp3 = int(input("Enter a num3: "))
##ar1.append(inp1)
##ar1.append(inp2)
##ar1.append(inp3)
##
##ar2 = array('i',[])
##for i in range(5):
##    n = random.randint(1,9)
##    ar2.append(n)
##
##ar1.extend(ar2)
##ar1 = sorted(ar1)
##for x in ar1:
##    print(x)


a1 = array('i', [])
a2 = array('i', [])

for i in range(5):
    inp = int(input("Enter a num: "))
    a1.append(inp)
a1 = sorted(a1)
print(a1)
r = int(input("Select one num : "))
if r in a1:
    a1.remove(r)
    a2.append(r)
    print(a1)
    print(a2)
else:
    print("This is not in the array")



##arr = array('i',[2, 4, 7, 1, 8, 5])
##print(arr)
##inp = int(input("Select one of the items: "))
##while not inp in arr:
##    print("Try again")
##    inp = int(input("Select one of the items: "))
##    
##ind = arr.index(inp)
##print("Position: ", ind)


##nums = array('f', [11.51, 23.16, 14.21, 34.76, 64.31])
##tryagain = True
##while tryagain == True:
##    inp = int(input("Enter a whole number between 2 and 5: "))
##    if inp<2 or inp>5:
##        print("Incorrect try again")
##    else:
##        tryagain = False
###        range(0, len(nums))
##for i in range(0, 5):
##    res = nums[i]/inp
##    print(round(res,2))





















