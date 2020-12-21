from tkinter import * 
import data_handling
from subprocess import call 
import tkinter.messagebox as tkmsgbox

# Getting data and the current user account id 
data = data_handling.get_data()
user_id = data_handling.get_userID()

def button_action() :
    window.quit()
    window.withdraw()
    call(["python", "option_window.py"])

###################### GUI ####################
# create and initialize show balance window
window = Tk() 
window.geometry("300x250+100+100")
window.title("ATM")
window.configure(background="#6495ED" 
              ,highlightbackground="#4682B4"
              ,highlightcolor="black")
window.resizable(width = False, height = False)

for i in range(0 , 2) :
    window.columnconfigure(i,minsize='10m')

for i in range(0 , 5) :
    window.rowconfigure(i,minsize='10m')

#Labels
text = '''Hi, {}
    Your balance is :
        {}
'''.format(data[user_id]['Name'] ,data[user_id]['balance'] )

welcome_label = Label(window ,text = text 
                      , font = 55 
                      , justify = LEFT
                      , fg = '#FF0000'
                      , bg = '#4682B4')
welcome_label.grid(row = 1, column = 0, columnspan = 2 ,sticky=W)

# Buttons 
enter_button = Button(window , text = "OK" 
                      , font = 30 
                      , command = button_action
                      , width = 25
                      , bg = '#4169E1' )
enter_button.grid(row = 3, column = 0 , columnspan = 2 )

mainloop()