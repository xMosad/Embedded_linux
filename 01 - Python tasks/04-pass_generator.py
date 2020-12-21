# Importing Tkinter module 
from tkinter import *
import random, string
import pyperclip

__pass = ""

def save_pass (ps) :
    f = open("pass.txt","a")
    f.write ("\n")
    f.write(ps) 
    f.close()

def check_pass (ps) :
    flag = 1 
    f = open("pass.txt","r")
    if ps in f.read() :
        flag = 0
        
    return flag 


# Generate configuration file 
# Called when the button is pressed 
def Generate () :
    global __pass
    password = ""
    pass_len = int (digits.get())
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)

    for y in range(pass_len- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    
    if check_pass(password) ==  0 :
        Generate()
    else :
        save_pass(password)
        _pass.configure(text = password)
        __pass = password
    


def copy () : 
     global __pass
     pyperclip.copy(__pass)
     

# Creating master Tkinter window 
window = Tk() 
window.geometry("450x200+100+100")
window.title("ATM")
window.configure(background="#6495ED" 
              ,highlightbackground="#4682B4"
              ,highlightcolor="black")
window.resizable(width = False, height = False)

for i in range(0 , 3) :
    window.columnconfigure(i,minsize='10m')

for i in range(0 , 9) :
    window.rowconfigure(i,minsize='10m')

#################### Creating GUI #####################

# Labels 
label1 = Label(window ,text = "Choose Number of digits" 
               , font = 55 
               , justify = LEFT
               , bg = '#4682B4')
label1.grid(row = 1,column = 0,sticky=W, columnspan = 2)

_pass = Label(window  
               , font = 55 
               , justify = LEFT
               , bg = '#4682B4')
_pass.grid(row = 4,column = 0, columnspan = 3)

# Spin box
digits = Spinbox(window
                 , from_= 8
                 , to = 32
                 , font = 60) 
digits.grid(row = 2,column = 1,sticky=W)

#Buttons
generate_button = Button(window , text = "Generate" 
                      , font = 10 
                      , command = Generate
                      , bd = 5
                      , bg = '#4169E1' )
generate_button.grid(row = 3, column = 1 )

copy_button = Button(window , text = "Copy" 
                      , font = 10 
                      , command = copy
                      , bd = 5
                      , bg = '#4169E1' )
copy_button.grid(row = 3, column = 2 )


mainloop()