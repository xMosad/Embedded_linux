from tkinter import * 
import data_handling
from subprocess import call 
import tkinter.messagebox as tkmsgbox

# Getting data and the current user account id 
data = data_handling.get_data()
user_id = data_handling.get_userID()
balance = int (data[user_id]['balance'])

def draw_money (m) :
    global balance
    # Update balance after withdrawing
    balance = balance - m 
    data[user_id]['balance'] = str (balance)
    data_handling.save_data(data)
    tkmsgbox.showinfo("Info", "Succesfull operation, Thank you!")
    window.quit()
    window.withdraw()
    call(["python", "option_window.py"])

def button_action() :
    global balance  
    money = input_money.get()
    money = int(money)
    
    # Check first if amount is under 5000
    if (money <= 5000) : 
        # Check if amount is multiple of 100L.E
        if ((money % 100 ) == 0) :
            # To check if the balance can cover the wanted money
            if (money < balance ) :
                draw_money(money)
            else :
                # If balance is not enough will return to the option window
                tkmsgbox.showwarning("Warning", "No sufficient balance")
                window.quit()
                window.withdraw()
                call(["python", "option_window.py"])
        else : 
            tkmsgbox.showwarning("Warning", "Allowed values are multiple of 100L.E")
            input_money.delete(0 , "end")
    else : 
        tkmsgbox.showwarning("Warning", "Max amount is 5000")
        input_money.delete(0 , "end")


###################### GUI ####################
# create and initialize cash withdraw window
window = Tk() 
window.geometry("500x320+100+100")
window.title("ATM")
window.configure(background="#6495ED" 
              ,highlightbackground="#6495ED"
              ,highlightcolor="black")
window.resizable(width = False, height = False)

for i in range(0 , 2) :
    window.columnconfigure(i,minsize='15m')

for i in range(0 , 5) :
    window.rowconfigure(i,minsize='15m')

#Labels
text = "Enter the amount of money "
welcome_label = Label(window ,text = text , font = 50 ,bg ='#87CEFA')
welcome_label.grid(row = 1, column = 0, columnspan = 2 ,sticky=W)

#Entery for the money
input_money = Entry(window,width = 15 , font = 30) 
input_money.grid(row = 2, column = 0 , columnspan = 2)

# Buttons 
enter_button = Button(window , text = "Enter" 
                      , font = 30 
                      , command = button_action
                      , width = 20
                      , bg = '#4169E1' 
                      , bd = 10)
enter_button.grid(row = 3, column = 0 , columnspan = 2 )

text = ''' Note that 
            1 - Max amount is 5000
            2 - Allowed values are multiple of 100L.E '''
Label(window ,text = text, font = 40 , justify = LEFT , bg ='#87CEFA').grid(row = 4, column = 1 )


mainloop()