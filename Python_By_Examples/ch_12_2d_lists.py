
##list_2d = [[2,5,8], [3,7,4], [1,6,9], [4,2,0]]
##r = int(input("Enter a row: "))
##print(list_2d[r])
##c = int(input("Enter a column: "))
##print(list_2d[r][c])
##ask = input("Want to change that value?(y/n): ")
##if ask == 'y':
##    new_val = int(input("Enter a new value: "))
##    list_2d[r][c] = new_val
##print(list_2d[r])


##sales_dict = {"John": {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
##              "Tom": {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
##              "Anne": {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
##              "Fiona": {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}}
##print(sales_dict)
##name = input("Enter a name: ")
##region = input("Enter a region: ")
##print("Sales: ", sales_dict[name][region])
##new_data = int(input("Enter a new data: "))
##sales_dict[name][region] = new_data
##print(sales_dict[name])


shoes = {}
for i in range(3):
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    size = int(input("Enter the shoe size: "))
    shoes[name] = {"Age": age, "Shoe size": size}
##for name in shoes:
##    print((name), shoes[name]["Age"])

ask = input("Enter a name to delete: ")
del shoes[ask]
for name in shoes:
    print(name, shoes[name]["Age"], shoes[name]["Shoe size"])
