from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()


# examples for updating the text on the label
my_label["text"] = "New Next"
my_label.config(text="New Text")

#button

def button_clicked():
    entry_txt = input.get()
    my_label.config(text=entry_txt)



button = Button(text="Click me", command=button_clicked)
button.pack()


# Entry field
input = Entry(width=10)
input.pack()
input.get()











window.mainloop()
