
##countries = ("Sweeden", "Germany", "Norway", "Italy", "France")
##print(countries)
##print(countries.index(input("Enter a country from list: ")))
##c_index = int(input("Enter the index: "))
##print(countries[c_index])


##subjects = ["math", "biology", "chemistry", "english", "literature", "sports"]
##print(subjects)
##del_subj = input("What subject do you want to delete?: ")
##subjects.remove(del_subj)
##   ind_to_del = subjects.index(del_subj)
##   del subjects[del_subj]
##print(subjects)


##food = {}
##for i in range(1,5):
##    user_inp = input("Enter your favourite food: ")
##    food[i] = user_inp
##print(food)
##user_inp = int(input("What you want to get rid of: "))
##del food[user_inp]
##print(sorted(food.values()))


##colors = []
##for i in range(10):
##    color_inp = input("Enter a color: ")
##    colors.append(color_inp)
##start_num = int(input("Enter a num between 0 an 4: "))
##end_num = int(input("Enter a num between 5 and 9: "))
##print(colors[start_num : end_num])


##numbers = [124, 476, 892, 251]
##for num in numbers:
##    print(num)
##user_inp = int(input("Enter a three-digit number: "))
##if user_inp in numbers:
##    print("Index of",user_inp,": ", numbers.index(user_inp))
##else:
##    print("That is not in the list")


##people = []
##print("Enter a nsmes of three people to invite:")
##people.append(input("1: "))
##people.append(input("2: "))
##people.append(input("3: "))
##cont = input("Wnat to add more (y/n): ")
##while cont == "y":
##    #people.append(input("Name: "))  can be used instead
##    new_name = people.append(input("name: "))
##    cont = input("Wnat to add more (y/n): ")
##print(len(people)," people coming to you party")
##
##print(people)
##name_inp = input("Enter a name from list: ")
##name_ind = people.index(name_inp)
##print(name_ind)
##q = input("Do you still want to invite this person? (y/n): ")
##if q == 'n':
##    people.remove(name_inp)
##    #del people[name_ind]
##print(people)


##tv_comp = ["show_sport", "show_science", "show_news", "show_music"]
##for show in tv_comp:
##    print(show)
##show = input("Enter another show: ")
##ind = int(input("Enter the index: "))
##tv_comp.insert(ind, show)
##print(tv_comp)


##numbers = []
##for i in range(3):
##    numbers.append(int(input("Enter num: ")))
##    print(numbers)
##a = input("Do you still want to save last number? (y/n): ")
##if a == 'n':
##    del numbers[len(numbers)-1]
##print(numbers)
#--------------------------------
numbers = []
count = 0
while count < 3:
    num = int(input("Enter a number: "))
    numbers.append(num)
    print(numbers)
    count = count + 1
lastnum = input("Do you still want last number saved? (y/n): ")
if lastnum == 'n':
    numbers.remove(num)
print(numbers)















