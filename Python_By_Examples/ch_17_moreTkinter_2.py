from tkinter import *
import random



def gen_question():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    res = num1 + num2

    text = "{:2d}".format(num1) + " + " + "{:2d}".format(num2)
    q_field.configure(state = "normal")
    q_field.insert(END, text)
    q_field.configure(state = "readonly")

    img = PhotoImage(file = "myLogo.gif")
    img_box.image = img
    img_box["image"] = img
    img_box.update()


def check_answ():
    answ = a_field.get()
    question = str(q_field.get())
    num_q = question.split(" + ")
    num1 = int(num_q[0].strip())
    num2 = int(num_q[-1].strip())
    res = num1 + num2
    
    if int(answ) == res:
        img = PhotoImage(file = "well_done_img.gif")
        img_box.image = img

    else:
        img = PhotoImage(file = "wrong_img.gif")
        img_box.image = img
    
    img_box["image"] = img
    img_box.update()

    a_field.delete(0, END)
    q_field.delete(0, END)


window = Tk()
window.geometry("500x400")
window.title("small_quiz")
window.configure(background = "light gray")

logo_img = PhotoImage(file = "myLogo.gif")

img_box = Label(window, image = logo_img)
img_box.image = logo_img
img_box.place(x = 150, y = 30, width = 200, height = 200)

question_b = Button(text = "Gen question:", command = gen_question)
question_b.place(x = 50, y = 250, width = 120, height = 25)

q_field = Entry(text = "")
q_field.place(x = 170, y = 250, width = 200, height = 25)
q_field["justify"] = "center"
q_field["relief"] = "flat"

a_field = Entry(text = "")
a_field.place(x = 170, y = 300, width = 200, height = 25)
a_field["justify"] = "center"
a_field["relief"] = "flat"

check_b = Button(text = "Check answer", command = check_answ)
check_b.place(x = 50, y = 300, width = 120, height = 25)

window.mainloop()

