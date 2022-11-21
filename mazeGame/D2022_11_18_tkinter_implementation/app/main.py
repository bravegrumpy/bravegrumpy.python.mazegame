from colors import Colors as c

# blue = c.BLUE
# chkStr = type(c.BLUE)


# c.CYAN = (0, 255, 255)

# chkStr = "Name: {name}, RGB{rgb}, nRGB{dec}".format(name='blue', rgb=c.BLUE, dec=c.rgb2dec(c, c.BLUE))
# print(chkStr)

clrs = c.get_all_clrs(c)
print(clrs)

import tkinter as tk
root = tk.Tk()

canvas = tk.Canvas(root, width=1000, height=500, background='#000000')

start = [10, 10]
end = [start[0] + 20, start[1] + 20]

for i in range(len(clrs)):
    canvas.create_rectangle(start[0], start[1], end[0], end[1], fill=c.rgb2hex(c, clrs[i]))
    start[0] = start[0] + 25
    end = [start[0] + 20, start[1] + 20]

label = tk.Label(root, text='Red', bg='#FF0000', fg='#FFFFFF')
button = tk.Button(root, text= 'THIS is a BUTTON')# , bg=c.rgb2hex(c,c.CYAN), fg=c.rgb2hex(c,c.BLUE))
canvas.pack(side=tk.BOTTOM)
label.pack(side=tk.TOP)
button.pack(side=tk.TOP)

root.mainloop()