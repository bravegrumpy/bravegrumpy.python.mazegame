import tkinter as tk
from tkinter import ttk


def define_grid(grd: int = 25, p: int = 25, m: float = 1.0):
    grid_size = grd
    pxls = grid_size * p
    size = (pxls, pxls)
    width = p
    height = p
    margin = m
    return size, width, height, margin


def obtain_data(var):
    print(var.get())


def create_grid_widgets(root):
    def obtain_grid_size():
        print(grid_size.get())
        return grid_size.get()

    grid_size = tk.IntVar()
    gridLabel = ttk.Label(root, text="Enter grid size:")
    gridEntry = ttk.Entry(root, textvariable=grid_size)
    gridButton = ttk.Button(root, text="Define Grid", command=obtain_grid_size)
    g = obtain_grid_size()
    return grid_size, gridLabel, gridEntry, gridButton, g
