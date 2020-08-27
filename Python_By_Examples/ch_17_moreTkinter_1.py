from tkinter import *




def hello_cm():
    name = name_txt.get()
    greeting = "Hello " + name.title() +"!"
    name_txt.delete(0, END)

    name_out.delete(0, END)
    name_out.insert(END, greeting)


window = Tk()
window.geometry("500x400")
window.title("Names")
window.configure(background = "light gray")

logo = PhotoImage(file = "200px_mylogo.gif")
logoimage = Label(image = logo)
logoimage.place(x = 150, y = 20, width = 200, height = 200)

label_1 = Label(text = "Enter your name:")
label_1.place(x = 50, y = 250, width = 120, height = 25)
label_1["bg"] = "light gray"

name_txt = Entry(text = "")
name_txt.place(x = 170, y = 250, width = 200, height = 25)
name_txt["justify"] = "center"
name_txt["relief"] = "flat"

name_out = Entry(text = "")
name_out.place(x = 170, y = 300, width = 200, height = 25)
name_out["justify"] = "center"
name_out["relief"] = "flat"

button_1 = Button(text = "Press me", command = hello_cm)
button_1.place(x = 50, y = 300, width = 120, height = 25)
