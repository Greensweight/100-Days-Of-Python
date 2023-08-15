from tkinter import *


def button_clicked():
    entry_txt = input.get()
    my_label.config(text=entry_txt)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=200)

#label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=100)


# examples for updating the text on the label
my_label["text"] = "New Next"
my_label.config(text="New Text")

#button

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)
# Entry field
input = Entry(width=10)
input.grid(column=3, row=2)
input.get()











window.mainloop()
