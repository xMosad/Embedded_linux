# Simple system for employee 
# App on Dict 

employee = {}
while (1) :
    print ("*************************************")
    print ("To add new empolyee press 1")
    print ("To print empolyee data press 2")
    print ("To delete empolyee press 3")
    print ("*************************************")
    press = input ("plz enter your choice : ")
    press = int(press)
    
    if (press == 1) :
        name   = input ("Enter name   : ")
        _id    = input ("Enter id     : ")
        _job   = input ("Enter job    : ")
        salary = input ("Enter salary : ")
        input ("Press any key.")
              
        employee [_id] = {
            "name"   : name ,
            "job"    : _job ,
            "salary" : salary ,
        }
        
    elif (press == 2) :
        _id = input ("Enter ID : ")
        if _id in employee : 
            print ("*************************************")
            print ("Employee Name   : " ,employee [_id]["name"])
            print ("Employee Job    : " ,employee [_id]["job"])
            print ("Employee Salary : " ,employee [_id]["salary"])
            print ("*************************************")
            input ("Press any key.")
        
        else : 
            print ("Wrong ID!")
            input ("Press any key.")
        
    elif (press == 3) :
        _id = input ("Enter ID : ")
        if _id in employee :
            del employee [_id]
        
        else :
            print ("Wrong ID!")
            input ("Press any key.")
    
    else :
        print ("Wrong choice!")
        break 
        
        
        
        
        