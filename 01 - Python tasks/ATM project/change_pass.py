from tkinter import * 
import data_handling
from subprocess import call 
import tkinter.messagebox as tkmsgbox

# Getting data and the current user account id 
data = data_handling.get_data()
user_id = data_handling.get_userID()

def button_action () :
    # To handle if the user entered values that are not integer
    try :
        pass1 = int ( new_pass1.get() )
        pass2 = int ( new_pass2.get() )
    except : 
        tkmsgbox.showwarning("Warning", "Passward is numbers only")
        new_pass1.delete(0 , "end")
        new_pass2.delete(0 , "end")
    
    # Fist ensure that pass is 4 digits 
    if (pass1 <= 9999) & (pass1 >= 1000) :
        # Check if pass was enterd twic the same
        if (pass1 == pass2) :
            # If new pass is not equal the old will change it
            if (pass1 != int (data[user_id]['pass'])) :
                data[user_id]['pass'] = str (pass1)
                data_handling.save_data(data)
                tkmsgbox.showinfo("Info", "Passward changed successfully")
                window.quit()
                window.withdraw()
                call(["python", "option_window.py"])
            else :
                tkmsgbox.showwarning("Warning", "New pass must ne different than the old one")
                new_pass1.delete(0 , "end")
                new_pass2.delete(0 , "end")
        else :
            tkmsgbox.showwarning("Warning", "Enter the passward agian right")
            new_pass1.delete(0 , "end")
            new_pass2.delete(0 , "end")
    else : 
        tkmsgbox.showwarning("Warning", "Passward is 4 digit only")
        new_pass1.delete(0 , "end")
        new_pass2.delete(0 , "end")


###################### GUI ####################
# create and initialize show balance window
window = Tk() 
window.geometry("500x300+100+100")
window.title("ATM")
window.configure(background="#6495ED" 
              ,highlightbackground="#4682B4"
              ,highlightcolor="black")
window.resizable(width = False, height = False)

for i in range(0 , 3) :
    window.columnconfigure(i,minsize='10m')

for i in range(0 , 6) :
    window.rowconfigure(i,minsize='10m')

#Labels
label0 = Label(window ,text = "Note pass is 4 digit only" 
               , font = 55 
               , justify = LEFT
               , fg = '#FF0000'
               , bg = '#4682B4')
label0.grid(row = 0,column = 0,sticky=W, columnspan = 2)

label1 = Label(window ,text = "Enter New pass         " 
               , font = 55 
               , justify = LEFT
               , bg = '#4682B4')
label1.grid(row = 1,column = 1,sticky=W)

label2 = Label(window ,text = "Enter New pass again" 
               , font = 55 
               , justify = LEFT
               , bg = '#4682B4')
label2.grid(row = 3,column = 1,sticky=W)

#Entery for the pass
new_pass1 = Entry(window,width = 15 , font = 30) 
new_pass1.grid(row = 1, column = 2 , columnspan = 2)

new_pass2 = Entry(window,width = 15 , font = 30) 
new_pass2.grid(row = 3, column = 2 , columnspan = 2)

# Buttons 
enter_button = Button(window , text = "Change" 
                      , font = 30 
                      , command = button_action
                      , width = 10
                      , bd = 5
                      , bg = '#4169E1' )
enter_button.grid(row = 5, column = 2 )

mainloop()