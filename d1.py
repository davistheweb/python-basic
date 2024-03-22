from tkinter import *


# Create the main tkinter window

root = Tk()
root.title("Registration Form")
root.geometry("300x300")
root.config(bg='cyan')
# Create a frame for the form
form_frame = Frame(root)
form_frame.pack(padx=10,
                pady=10,
                fill="both",
                expand=True)

# Create labels and entry fields for each input
Username_label = Label(form_frame, text="Username:")
Username_label.grid(row=0, column=0, sticky="w")
Username_entry = Entry(form_frame)
Username_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

Password_label = Label(form_frame, text="Password:")
Password_label.grid(row=1, column=0, sticky="w")
Password_entry = Entry(form_frame)
Password_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

submit_button = Button(form_frame, text="Submit")
submit_button.grid(row=2, columnspan=2, pady=10)

if __name__ == "_main_":
   root.mainloop()