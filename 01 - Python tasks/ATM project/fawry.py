from tkinter import *
from tkinter import ttk 
import data_handling
from subprocess import call 
import tkinter.messagebox as tkmsgbox

# Getting data and the current user account id 
data = data_handling.get_data()
user_id = data_handling.get_userID()

def button_action () :
    balance = int (data[user_id]['balance'])
    # To handle if the amount or the number are not integral values
    try :
        number = int (input_number.get())
        money = int (input_money.get())
    except : 
        tkmsgbox.showwarning("Warning", "Number or money are not valid values")
        input_number.delete(0 , "end")
        input_money.delete(0 , "end")
    
    # Check number of digits of the phone number      
    if ((number <= 99999999) & (number >= 10000000)) : 
        # Check first if the balance covers the charge
        if (money <= balance):
            balance = balance - money 
            data[user_id]['balance'] = str (balance)
            data_handling.save_data(data)
            tkmsgbox.showinfo("Info", "Charged successfully")
            window.quit()
            window.withdraw()
            call(["python", "option_window.py"])
        else  :
            tkmsgbox.showwarning("Warning", "Not sufficient balance")
            window.quit()
            window.withdraw()
            call(["python", "option_window.py"])
    else : 
        tkmsgbox.showwarning("Warning", "Number is not valid")
        input_number.delete(0 , "end")

 
  
def choose_company () : 
    text = company.get()
    if text == 'Orange' :
        label4.configure(text = "012")
    elif text == 'Vodafone' :
        label4.configure(text = "010")
    elif text == 'Etisalat':
        label4.configure(text = "011")
    elif text == 'We':
        label4.configure(text = "015")

###################### GUI ####################
# create and initialize show balance window
window = Tk() 
window.geometry("550x400+100+100")
window.title("ATM")
window.configure(background="#6495ED" 
              ,highlightbackground="#4682B4"
              ,highlightcolor="black")
window.resizable(width = False, height = False)

for i in range(0 , 3) :
    window.columnconfigure(i,minsize='10m')

for i in range(0 , 9) :
    window.rowconfigure(i,minsize='10m')

#Labels
label1 = Label(window ,text = "Choose your company" 
               , font = 55 
               , justify = LEFT
               , bg = '#4682B4')
label1.grid(row = 1,column = 0,sticky=W, columnspan = 2)

label2 = Label(window ,text = "Enter your number" 
               , font = 55 
               , justify = LEFT
               , bg = '#4682B4')
label2.grid(row = 3,column = 0,sticky=W)

label3 = Label(window ,text = "Enter charge amount" 
               , font = 55 
               , justify = LEFT
               , bg = '#4682B4')
label3.grid(row = 5,column = 0,sticky=W)

label4 = Label(window ,text = "010" 
               , font = 55 
               , justify = LEFT
               , bg = '#4682B4')
label4.grid(row = 4,column = 0,sticky=E)

#Entery for the money
input_number = Entry(window,width = 15 , font = 30) 
input_number.grid(row = 4, column = 1  ,sticky=W)

input_money = Entry(window,width = 15 , font = 30) 
input_money.grid(row = 6, column = 1  ,sticky=W)

# Combobox
n = StringVar() 
company = ttk.Combobox(window, width = 18
                   , font = 30 
				   ,textvariable = n)
                            # Adding combobox drop down list 
company['values'] = ('Orange', 
                     'Vodafone', 
					 'Etisalat', 
					 'We' )  

company.grid(column = 1, row = 2)
company.current(1)

# Buttons 
enter_button = Button(window , text = "Charge" 
                      , font = 30 
                      , command = button_action
                      , width = 10
                      , bd = 5
                      , bg = '#4169E1' )
enter_button.grid(row = 7, column = 1 )

select_button = Button(window , text = "Select" 
                      , font = 10 
                      , command = choose_company
                      , bd = 5
                      , bg = '#4169E1' )
select_button.grid(row = 2, column = 2 )

mainloop()

 