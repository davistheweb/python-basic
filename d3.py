from tkinter import *

root = Tk()
root.title("Registration Form")
root.geometry("300x300")
root.config(bg='red')

# Create a frame for the form
form_frame = Frame(root)
form_frame.pack(padx=10, pady=10)

# Heading
heading_label = Label(form_frame, text="Registration", font=("Helvetica", 16, "bold"))
heading_label.pack()

# Labels
Name_label = Label(form_frame, text="Name:")
Name_label.pack()

Course_label = Label(form_frame, text="Course:")
Course_label.pack()

Score_label = Label(form_frame, text="Score:")
Score_label.pack()

# Button
submit_button = Button(form_frame, text="Insert")
submit_button.pack(pady=10)

root.mainloop()