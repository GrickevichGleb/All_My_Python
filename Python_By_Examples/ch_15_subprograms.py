
import random
import csv

##def get_num():
##    num = int(input("Enter a number: "))
##    return num
##
##def count_to_num(num):
##    i = 1
##    while i <= num:
##        print(i)
##        i = i + 1
##
##def main():
##    n = get_num()
##    count_to_num(n)
##    
##main()


##def pick_num():
##    low = int(input("Enter a low number: "))
##    high = int(input("Enter a high number: "))
##    comp_num = random.randint(low, high)
##    return comp_num
##
##def gues_n():
##    gues_num = int(input("I am thinking of a number: "))
##    return gues_num
##
##def check_n(comp_n, gues_n):
##    again = True
##    while again == True:
##        if comp_n == gues_n:
##            print("Correct you win")
##            again = False
##        elif comp_n > gues_n:
##            gues_n = int(input("Too low, try again: "))
##        else:
##            gues_n = int(input("Too high, try again: "))
##
##def main():
##    comp_num = pick_num()
##    gues_num = gues_n()
##    check_n(comp_num, gues_num)
##
##main()
    


##def addition_prog():
##    a = random.randint(5, 20)
##    b = random.randint(5, 20)
##    correct_a = a + b
##    print(a, "+", b, )
##    user_a = int(input("Your answer: "))
##    res = (correct_a, user_a)
##    return res
##
##def substraction_prog():
##    a = random.randint(25, 50)
##    b = random.randint(1, 25)
##    correct_a = a - b
##    print(a, "-", b)
##    user_a = int(input("Your answer: "))
##    res = (correct_a, user_a)
##    return res
##
##def check_prog(correct, user):
##    if correct == user:
##        print("Correct")
##    else:
##        print("Incorrect, the answer is: ", correct)
##
##def main():
##    print("1) Addition")
##    print("2) Substraction")
##    p = int(input("Enter 1 or 2: "))
##
##    if p == 1:
##        correct, user = addition_prog()
##        check_prog(correct, user)
##    elif p == 2:
##        correct, user = substraction_prog()
##        check_prog(correct, user)
##    else:
##        print("Error")
##
##main()


##def add_name():
##    name = input("Enter name: ")
##    names.append(name)
##    return names
##
##def change_name():
##    num = 0
##    for x in names:
##        print(num, x)
##        num = num + 1
##    select_num = int(input("Enter the number of the name you want to change: "))
##    name = input("Enter a new name: ")
##    names[select_num] = name
##    return names
##
##def delete_name():
##    num = 0
##    for x in names:
##        print(num, x)
##        num = num + 1
##    selected_num = int(input("Enter the number of the name you want to delete: "))
##    del names[selected_num]
##    return names
##
##def view_names():
##    for x in names:
##        print(x)
##    print()
##
##def main():
##    again = 'y'
##    while again == 'y':
##        print("1) Add a name")
##        print("2) Change a name")
##        print("3) Delete a name")
##        print("4) View names")
##        print("5) Quit")
##        selection = int(input("What do you want to do?: "))
##        if selection == 1:
##            names = add_name()
##        elif selection == 2:
##            names = change_name()
##        elif selection == 3:
##            names = delete_name()
##        elif selection == 4:
##            names = view_names()
##        elif selection == 5:
##            again = 'n'
##        else:
##            print("Incorrect option")
##        data = (names, again)
##
##names = []
##main()




def add_to_file():
    name = input("Enter your name: ")
    salarie = input("Enter salarie: ")
    file = open("Salaries.csv", 'a')
    file.write(str(name+','+salarie+'\n'))
    file.close()

def delete_from_file():
    file = open("Salaries.csv", 'r')
    tmp = []
    for line in file:
        tmp.append(line)
    file.close()
    num = 0
    for x in tmp:
        print(num, x)
        num = num + 1
    ind = int(input("What line would you delete?: "))
    del tmp[ind]

    file = open("Salaries.csv", "w")
    for rec in tmp:
        file.write(rec)
    file.close()

def read_records():
    file = open("Salaries.csv", 'r')
    for row in file:
        print(row)
    file.close()

def main():
    
    cont = 'y'
    while cont == 'y':
        print("\nOptions menu:")
        print("1) Add to file")
        print("2) Delete from file")
        print("3) View all records")
        print("4) Quit program")
        inp = int(input("Enter a number of selection: "))
        if inp == 1:
            add_to_file()
        elif inp == 2:
            delete_from_file()
        elif inp == 3:
            read_records()
        elif inp == 4:
            cont = 'n'
        else:
            print("Error")

main()






















   
