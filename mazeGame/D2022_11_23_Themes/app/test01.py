import tkinter as tk

import ttkbootstrap as ttk
# from tkinter import ttk

def change_theme():
    root.style.theme_use(root.selected_theme.get())


root = tk.Tk()
root.title("Theme Demo")
root.geometry('400x300')
root.style = ttk.Style()

# label
label = ttk.Label(root, text='Name: ')
label.grid(column=0, row=0, padx=10, pady=10, sticky='w')
# entry
textbox = ttk.Entry(root)
textbox.grid(column=1, row=0, padx=10, pady=10, sticky='w')

# button
btn = ttk.Button(root, text='Show')
btn.grid(column=2, row=0, padx=10, pady=10, sticky='w')

# radio button
root.selected_theme = tk.StringVar()
theme_frame = ttk.LabelFrame(root, text='Themes')
theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=10, sticky='w')

# radio buttons
for theme_name in root.style.theme_names():
    rb = ttk.Radiobutton(
        theme_frame,
        text=theme_name,
        value=theme_name,
        variable=root.selected_theme,
        bootstyle="outline-toolbutton",
        command=change_theme)
    rb.pack(expand=True, fill='both')

root.mainloop()
