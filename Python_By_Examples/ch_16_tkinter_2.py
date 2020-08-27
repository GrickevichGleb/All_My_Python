from tkinter import *


def add_name():
    name = name_box.get()
    name_list.insert(END, name)
    name_box.delete(0, END)
    name_box.focus()

def clear_list():
    name_list.delete(0, END)
    name_box.focus()

window = Tk()
window.title("List App")
window.geometry("500x300")

label_1 = Label(text = "Enter your name:")
label_1.place(x = 30, y = 20, width = 150, height = 25)

name_list = Listbox()
name_list.place(x = 30, y = 50, width = 150, height = 200)

name_box = Entry(text = "")
name_box.place(x = 190, y = 20, width = 150, height = 25)
name_box["justify"] = "center"
name_box.focus()

btn_1 = Button(text = "Add name", command = add_name)
btn_1.place(x = 190, y = 50, width = 100, height = 25)

btn_2 = Button(text = "Clear list", command = clear_list)
btn_2.place(x = 190, y = 80, width = 100, height = 25)

window.mainloop()
