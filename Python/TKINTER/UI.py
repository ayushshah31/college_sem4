from tkinter import *
import tkinter as tk
import tkinter.font as Tkfont

# def clickMe():
#     print("Button CLick")


def clickMe():
    myLabel.grid_forget()


def submit():
    print(selected.get())
    print(myEntry1.get())
    print(myEntry2.get())
    print(dropDown_select.get())


def myValidate():
    print("In Validate")
    if(len(myEntry1.get()) > 1):
        print("True")
        return True
    else:
        print("In False")
        return False


window = Tk()
window.title('Demo')
window["bg"] = "gold"

# myLabel = Label(text="Hello", background='blue', font=("Helvetica", 50))
# myEntry = Entry()
# myEntry.grid(row=2, column=2)
# mybutton = Button(text='Click Me', command=lambda: clickMe())
# mybuttonSubmit = Button(text='Submit', command=lambda: submit())


# myLabel.place(x=0, y=20)
# mybutton.place(x=10, y=50)
# myLabel.grid(row=1, column=1)
# mybutton.grid(row=3, column=3)
# mybuttonSubmit.grid(row=3, column=2)
# mybutton.grid(column=20, columnspan=10, row=10, rowspan=10)
# myLabel1 = Label(text="Text 2")
# myLabel1.grid(row=4, column=5)

name = Label(text='Name')
name.grid(row=1, column=1)
myEntry1 = Entry()
myEntry1.grid(row=1, column=2)

password = Label(text='Password')
password.grid(row=3, column=1)
myEntry2 = Entry(validate='focusout', validatecommand=lambda: myValidate())
myEntry2.grid(row=3, column=2)

selected = tk.StringVar()
radio1 = tk.Radiobutton(window, text='Male', value='Male', variable=selected)
radio2 = tk.Radiobutton(window, text='Female',
                        value='Female', variable=selected)

radio1.grid(row=4, column=2)
radio2.grid(row=6, column=2)

mybuttonSubmit = Button(text='Submit', command=lambda: submit())
mybuttonSubmit.grid(column=20, columnspan=10, row=10, rowspan=10)


options = ['Monday', "Tuesday", "Wednesday"]
dropDown_select = tk.StringVar()
drop = OptionMenu(window, dropDown_select, *options)
drop.grid(row=5, column=5)

window.geometry("500x500")
window.mainloop()
