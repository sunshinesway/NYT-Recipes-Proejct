import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import scrolledtext


root = tk.Tk()
w = 400
h = 500 

# get screen width and height
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight() 

# calculate x and y coordinates for window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the window
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.resizable(width=False, height=False)
filler = tk.Label(text="")
filler.grid(row=0, padx=5, pady=5)

# Title Label
ttk.Label(root, 
          text = "ScrolledText Widget Example",
          font = ("Arial", 15), 
          background = 'green', 
          foreground = "white").grid(column = 0,
                                     row = 0)

# Creating scrolled text 
# area widget
text_area = scrolledtext.ScrolledText(root, 
                                      wrap = tk.WORD, 
                                      width = 40, 
                                      height = 10, 
                                      font = ("Arial", 15) )

text_area.grid(column = 0, pady = 10, padx = 10)
# Making the text read only
text_area.configure(state ='disabled')

# Placing cursor in the text area
text_area.focus()
root.mainloop()

