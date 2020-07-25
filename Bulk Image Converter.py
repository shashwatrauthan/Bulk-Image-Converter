# Shashwat Rauthan     <<BULK IMAGE CONVERTER GUI APPLICATION>>

import os
import tkinter as tk
from tkinter import ttk,filedialog,messagebox
from PIL import Image

win = tk.Tk()
win.geometry("300x250")
win.title("Image Converter")
icon = tk.PhotoImage(file = r"C:\Users\shash\Desktop\Python\convert.png")
win.iconphoto(True,icon)



filepath_label = ttk.Label(text = "Set Folder Path")
filepath_label.grid(row = 0,columnspan = 2,padx = 100,pady = 20)

path = tk.StringVar()
filepath_text = ttk.Entry(width = 35,textvariable = path)
filepath_text.focus()
filepath_text.grid(row = 1,column = 0,padx = 20)

def set_path():
    directory = filedialog.askdirectory(initial = os.getcwd)
    path.set(directory)

path_icon = tk.PhotoImage(file = r"C:\Users\shash\Desktop\Python\open.png")
path_button = ttk.Button(image = path_icon ,command = set_path)
path_button.grid(row = 1,column = 1,sticky = tk.W)

filetype_label = ttk.Label(text = "Select Output Type")
filetype_label.grid(row = 3,columnspan = 2,pady = 20)

file_type = tk.StringVar()
file_type.set('.jpg')

filetype_text = ttk.Radiobutton(text = 'JPG',value = '.jpg',variable = file_type)
filetype_text.grid(row = 4,columnspan = 2,padx = 65,sticky = tk.W)
filetype2_text = ttk.Radiobutton(text = 'PNG',value = '.png',variable = file_type)
filetype2_text.grid(row = 4,columnspan = 2,padx = 65,sticky = tk.E)


def process():
    file_path = path.get()
    file_type_ = file_type.get()
    os.chdir(file_path)
    if not os.path.exists('Converted Files'):
        os.mkdir('Converted Files')
    types = ('.jpg','.png','.jpeg','.ico')
    for i in os.listdir():
        if i.endswith(types):
            img = Image.open(i)
            name,extension = i.split('.')
            file_name = name+file_type_
            directory = os.path.join(os.getcwd(),'Converted Files',file_name)
            img.save(directory)
    
    messagebox.showinfo('Info','Task Completed!')


button = ttk.Button(text = 'Convert' ,command = process)
button.grid(row = 5,columnspan = 2,pady = 20)

win.mainloop()