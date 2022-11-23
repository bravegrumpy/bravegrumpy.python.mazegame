from colors import Colors as c
import tkinter as tk
from tkinter import ttk
from draw_maze import define_grid, obtain_data

root = tk.Tk()


def obtain_grid_size():
    if grid_size.get() == 0:
        print("If grid_size == 0, grid_size = {g}".format(g=grid_size.get()))
        return 25
    else:
        print("If grid_size != 0, grid_size = {g}".format(g=grid_size.get()))
        return grid_size.get()


grid_size = tk.IntVar()
gridLabel = ttk.Label(root, text="Enter grid size:")
gridEntry = ttk.Entry(root, textvariable=grid_size)
gridButton = ttk.Button(root, text="Define Grid", command=obtain_grid_size)
g = obtain_grid_size()
print("The value g = {g}, when obtained calling the 'obtain_grid_size' function.".format(g=g))

s, w, h, m = define_grid(int(25), int(20))

canvas = tk.Canvas(root, width=s[0], height=s[1], background=c.rgb2hex(c, c.BLACK))
canvas.create_rectangle(10, 10, 10 + w, 10 + h, fill=c.rgb2hex(c, c.MAGENTA))

gridLabel.grid(row=0, rowspan=1, column=0, columnspan=1)
gridEntry.grid(row=0, rowspan=1, column=1, columnspan=1)
gridButton.grid(row=0, rowspan=1, column=2, columnspan=1)
canvas.grid(row=2, rowspan=5, column=0, columnspan=5)
root.mainloop()
