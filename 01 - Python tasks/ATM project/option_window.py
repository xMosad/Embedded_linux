from tkinter import *
from subprocess import call 
import data_handling

# Getting data and the current user account id 
data = data_handling.get_data()
user_id = data_handling.get_userID()

# Every button will guide the user to specific service 
# Every specific service is implemented in script 

def withdraw_cash () :
    window.quit()
    window.withdraw()
    call(["python", "cash_withdraw.py"])
    
    
def balance_inq () :
    window.quit()
    window.withdraw()
    call(["python", "show_balance.py"])
    

def change_pass () :
    window.quit()
    window.withdraw()
    call(["python", "change_pass.py"])
    
def fawry_s () :
    window.quit()
    window.withdraw()
    call(["python", "fawry.py"])
    
def _exit () :
    window.quit()
    window.withdraw()
    data_handling.set_userID('')
    call(["python", "main.py"])

###################### GUI ####################
# create and initialize choose window
window = Tk() 
window.geometry("500x500+100+100")
window.title("ATM")
window.configure(background="#6495ED" 
              ,highlightbackground="#6495ED"
              ,highlightcolor="black")
window.resizable(width = False, height = False)

for i in range(0 , 3) :
    window.columnconfigure(i,minsize='15m')

for i in range(0 , 8) :
    window.rowconfigure(i,minsize='15m')

#Labels
text = "Hello, " + data[user_id]['Name']
welcome_label = Label(window ,text = text 
                      , font = 50 
                      , bg ='#87CEFA')
welcome_label.grid(row = 0, column = 0)

Label(window ,text = "Choose your service" 
     , font = 50 
     , bg ='#87CEFA').grid(row = 1, column = 1)

# Buttons 
withdraw = Button(window , text = "Withdraw Cash" 
                  , font = 30 
                  , command = withdraw_cash
                  , width = 30
                  , bg = '#4169E1' 
                  , bd = 10)
withdraw.grid(row = 2, column = 0,columnspan = 3)

balance = Button(window , text = "Show balance" 
                 , font = 30 
                 , command = balance_inq
                 , width = 30
                 , bg = '#4169E1' 
                 , bd = 10)
balance.grid(row = 3, column = 0,columnspan = 3)

pass_change = Button(window , text = "Change pass" 
                     , font = 30 
                     , command = change_pass
                     , width = 30
                     , bg = '#4169E1' 
                     , bd = 10)
pass_change.grid(row = 4, column = 0,columnspan = 3)

fawry = Button(window , text = "Fawry services" 
               , font = 30 
               , command = fawry_s
               , width = 30
               , bg = '#4169E1' 
               , bd = 10)
fawry.grid(row = 5, column = 0,columnspan = 3)

exit_p = Button(window , text = "Exit" 
                , font = 30 
                , command = _exit
                , width = 30
                , bg = '#4169E1' 
                , bd = 10)
exit_p.grid(row = 6, column = 0,columnspan = 3)

mainloop()