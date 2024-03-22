from tkinter import *


root = Tk()
root.title("Menu and Registration Form")
root.geometry("300x300")
root.config(bg='midnightblue')
# Create a frame for the form
form_frame = Frame(root)
form_frame.pack(padx=10, pady=10, fill="both", expand=True)

menu_frame = Frame(root)
menu_frame.pack(padx=10, pady=10, fill="both", expand=True)


menu_button = Button(menu_frame, text="MENU",)
menu_button.grid(row=2, columnspan=2, pady=10)

registration_button = Button(form_frame, text="REGISTRATION",)
registration_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()