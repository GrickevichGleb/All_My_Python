from tkinter import *


def add_num():
    num = text_box.get()
    if num.isdigit():
        list_box.insert(END, num)
        text_box.delete(0, END)
        text_box.focus()
    else:
        text_box.delete(0, END)
        text_box.focus()

def clr_list():
    list_box.delete(0, END)
    text_box.focus()

def save_list():
    tmp_list = list_box.get(0, END)
    file = open("list_num.csv", "a")
    for num in tmp_list:
        new_line = str(num) + "\n"
        file.write(new_line)
    file.close()

    list_box.delete(0, END)

window = Tk()
window.title("isDigit?")
window.geometry("400x400")

label_1 = Label(text = "Enter number:")
label_1.place(x=20, y=10, width=120, height=25)

text_box = Entry(text = 0)
text_box.place(x=145, y=10, width=170, height=25)

list_box = Listbox()
list_box.place(x = 20, y = 40, width = 120, height = 200)

add_button = Button(text = "Add", command = add_num)
add_button.place(x = 145, y = 40, width = 80, height = 25)

clr_button = Button(text = "Clear", command = clr_list)
clr_button.place(x = 230, y = 40, width = 80, height = 25)

save_button = Button(text = "Save", command = save_list)
save_button.place(x = 145, y = 70, width = 170, height = 25)
