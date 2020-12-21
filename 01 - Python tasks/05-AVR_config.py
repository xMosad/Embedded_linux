# Importing Tkinter module 
from tkinter import *

# Generate configuration file 
# Called when the button is pressed 
def configure () :
    file = open ("int.c" , "a")
    file.write("void init_porta(void)\n")
    file.write("{\n")
    file.write("\tDDRA = 0b")
    for i in v :
        if i.get() == "in" :
            file.write("0")
        
        elif i.get() == "out" :
            file.write("1")
        
    file.write(";\n}") 
    file.close()

# Creating master Tkinter window 
master = Tk() 
master.geometry("500x350+50+50") 
master.title("AVR Configuration")
master.resizable(width = False, height = False)


#################### Creating GUI #####################

Label(master, text =" * Configuration of PORTA *" , font = 50).grid(row = 0 , column = 1)

# Creating labels 
for i in range(1 , 9) : 
    text = "Configure Bit" + str((i-1))
    Label(master, text =text , font = 50).grid(row = i, column = 0)

# Initialize variables for radio buttons 
v  = [StringVar(master, "in"), 
      StringVar(master, "in"),
      StringVar(master, "in"),
      StringVar(master, "in"),
      StringVar(master, "in"),
      StringVar(master, "in"),
      StringVar(master, "in"),
      StringVar(master, "in")]
  
# creating radio buttons  
for i in range(1,9): 
    Radiobutton(master, text = "INPUT", variable = v[(i-1)], value = "in",  background = "light blue").grid(row =i, column = 1) 

for i in range(1,9): 
    Radiobutton(master, text = "OUTPUT", variable = v[(i-1)], value = "out",  background = "light blue").grid(row =i, column = 2) 
  
# Creating and placing button 
master.rowconfigure(9 , minsize='20')  
Button(master, text ='Create file' , font = 50 , command = configure).grid(row = 10, column = 1)

mainloop()