import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Python GUI")
window.geometry("700x500+100+50")
window.config(bg='cyan')
label = tk.Label(window,
               text="name",
               background='#12ddee',
               height='1',
               font=("Roman", 15, "bold"
                     )
               )
label.grid(column=0,
         ipadx=5,
         row=0,
         padx=5,
         pady=5
         )


def clicked():
    label.configure(text="SUBMITTED")


btn = tk.Button(window,
                text="Submit",
                background="#12ddee",
                padx=5,
                pady=5,
                command=clicked
                )
btn.grid(column=2,
         row=0,
         padx=10,
         pady=1
         )

txt = tk.Entry(window,
               width=10
               )
txt.grid(column=1,
         row=0
         )
txt.focus()

txt_disabled = tk.Entry(window,
                        width=10,
                        state='disabled'
                        )
txt_disabled.grid(column=4,
                  row=0
                  )

combo = ttk.Combobox(window)
combo["values"] = (1, 2, 3,)
combo.current(1)  # Set selected item
combo.grid(column=3,
           row=0
           )

# Checkbox
chk_state = tk.BooleanVar()
chk_state.set(True)  # Set check state
chk = tk.Checkbutton(window,
                     text="choose",
                     variable=chk_state
                     )
chk.grid(column=5,
         row=0
         )

# RadioButtons
rad1 = tk.Radiobutton(window,
                      text='First',
                      value=1
                      )
rad2 = tk.Radiobutton(window,
                      text='Second',
                      value=2
                      )
rad3 = tk.Radiobutton(window,
                      text='Third',
                      value=3
                      )
rad1.grid(column=6,
          row=0
          )
rad2.grid(column=7,
          row=0
          )
rad3.grid(column=8,
          row=0
          )
window.mainloop()
