from tkinter import *


def convert_1():
    ml = miles_txt.get()
    ml = int(ml)
    result_km = ml * 1.6093
    
    kilometers_txt.delete(0, END)
    kilometers_txt.insert(END, result_km)
      
def convert_2():
    km = kilometers_txt.get()
    km = int(km)
    result = km * 0.6214

    miles_txt.delete(0, END)
    miles_txt.insert(END, result)

    
window = Tk()
window.geometry("600x250")
window.title("Miles/Kilometers Converter")

label_1 = Label(text = "Enter miles:")
label_1.place(x = 20, y = 20, width = 120, height = 25)

miles_txt = Entry(text ="")
miles_txt.place(x = 150, y = 20, width = 100, height = 25)
miles_txt["justify"] = "center"

label_2 = Label(text = "Enter kilometers:")
label_2.place(x = 20, y = 50, width = 120, height = 25)

kilometers_txt = Entry(text = "")
kilometers_txt.place(x = 150, y = 50, width = 100, height = 25)
kilometers_txt["justify"] = "center"

button_1 = Button(text = "Mil to Km", command = convert_1)
button_1.place(x = 255, y = 20, width = 80, height = 25)

button_2 = Button(text = "Km to Mil", command = convert_2)
button_2.place(x = 255, y = 50, width = 80, height = 25)

window.mainloop()
