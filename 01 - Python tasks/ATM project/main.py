from tkinter import * 
import tkinter.messagebox as tkmsgbox
import csv
from subprocess import call
import data_handling

# Getting data of the users 
data = data_handling.get_data()

# Global varaiables 
flag = 0
error_count = 0
input_id = ""

# Checking the pass will be called after entering the account right 
# Will check if the enterd pass equels the stored pass in data 
def check_pass () :
    global input_id
    global error_count
    input_pass = input_account.get()
    
    # If the eneterd pass is correct will branch to the option window 
    if input_pass == data[input_id]['pass'] :
        main.quit()
        main.withdraw()
        data_handling.set_userID(input_id)
        call(["python", "option_window.py"])
        
    # if pass is wrong will notify the user of the remaining times he can try 
    else :
        # Store how many time the pass was enterd wrong
        error_count += 1 
        tries = str ((3 - error_count ))
        tkmsgbox.askretrycancel("Warning", "Wrong password you have " + tries + "tries left")
        input_account.delete(0 , "end")
    
    # To terminate the program if the user eneterd the pass three times wrong 
    # Will block the account
    if error_count == 3 : 
        tkmsgbox.showinfo("Info", "Sorry, this account has been blocked")
        data[input_id]['state'] = 'B'
        data_handling.save_data(data)
        main.destroy()

# Check if the eneterd account match any account in the system 
# If matched the screen will ask user to enter the pass     
def check_account (): 
    global flag 
    global input_id 
    input_id = input_account.get()
    
    if input_id in data :
        #  Check first if the account is blocked or not 
        if data[input_id]['state'] == 'N' :
            label_acccount.config(text = "Enter the password")
            input_account.config(show = '*')
            input_account.delete(0 , "end") # Clear the entry 
            # Setting the flag to change action of the button to check_pass
            flag = 1
        
        # To block the user if the account is blocked 
        elif data[input_id]['state'] == 'B' :
            tkmsgbox.showinfo("Warning", "This account has been blocked")
    else : 
        tkmsgbox.showwarning("Warning", "This account ID doesn't exist!")


def button_action () : 
    global flag 
    # Excuted first to check input account 
    if flag == 0 : 
        check_account()
        
    # If the account is entered correct will then check on the pass 
    elif flag == 1 :
        check_pass()    
    

# create and initialize main window
main = Tk() 
main.geometry("500x350+100+100")
main.title("ATM")
main.configure(background="#6495ED" 
              ,highlightbackground="#6495ED"
              ,highlightcolor="black")
main.resizable(width = False, height = False)


for i in range(0 , 4) :
    main.columnconfigure(i,minsize='20m')
    main.rowconfigure(i,minsize='20m')

# main image
photo = PhotoImage(file = "D:\\xBlank\\COM\\Linux\\01 - Python labs\\#project1-python\\img1.png")
photo = photo.subsample(2, 2)   
Label(main ,image = photo ).grid(columnspan = 4 , row = 0, column = 0)

# Labels 
label_acccount = Label(main ,text = "Enter your account ID" , font = 30 , bg ='#87CEFA' )
label_acccount.grid(row = 1, column = 1 , sticky=W)

#Entry 
input_account = Entry(main,width = 15 , font = 30)
input_account.grid(row = 1, column = 2)

#Buttons
enter_button = Button(main , text = "Enter" 
                      , font = 30 
                      , width = 10
                      , command = button_action 
                      , bg = '#4169E1' 
                      , bd = 10)
enter_button.grid(row = 2, column = 0,columnspan = 4)

mainloop()