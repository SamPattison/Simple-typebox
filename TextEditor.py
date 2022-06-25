import tkinter.messagebox
from tkinter import *
from tkinter.filedialog import *

filename = None
def newfile(): # Defining the 'new file' function
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def openfile():  # Defining the 'open file' function
    global filename
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.delete(0., END)

def savefile(): # Defining the 'save file' function
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveas(): # Defining the 'save as' function
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip()) # This keeps all the white space below the text
    except:
        tkinter.messagebox.showerror(Label='Error', message = 'Unable to save file.')

root = Tk()
root.title("Simple Text Editor")
root.minsize(width=600, height=600)
root.maxsize(width=600, height=600)

text = Text(root, width=600, height=600)
text.pack() # Opens the text box

my_menu = Menu(root) # Configuring the menubar
root.config(menu=my_menu)
file_menu = Menu(my_menu)

my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=newfile)
file_menu.add_command(label='Open', command=openfile)
file_menu.add_command(label='Save', command=savefile)
file_menu.add_command(label='Save as', command=saveas)
file_menu.add_separator()
file_menu.add_command(label='Quit', command=root.quit)

root.mainloop()

