from tkinter import *
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"



#--------------------------UI Setup---------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)

canvas = Canvas(width=800, height=526)
logo_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)

# Add the x button

window.mainloop()
