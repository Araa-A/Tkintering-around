# Write your code here :-)
import tkinter as tk
from tkinter import ttk

# Finally learning Tkinter! This is going to be a long term break... (if only the term break itself were long, hah.)

# window
window = tk.Tk()
window.title('Demo')
window.geometry('300x150') # string wants a width and a height seperated by an x

# title
title_label = ttk.Label(master = window, text = 'Mile to Kilometers', font =  'Calibri 24 bold')
# label means text
# label needs to be in container, which is the main window for now
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button= ttk.Button(master = input_frame, text = 'Convert')
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left') # packs within input_frame
input_frame.pack(pady = 10) # packs within window


# output
output_label = ttk.Label(master = window, text = 'Output',font =  'Calibri 24')
output_label.pack(pady = 10)


#  run
window.mainloop() # why does this remind me of voidloop() from C++ ...
