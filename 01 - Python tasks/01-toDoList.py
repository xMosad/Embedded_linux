
toDoList = []
doneList = []
while (1) : 
    print ("|*****************************|")
    print ("To add new item press 1")
    print ("To print the to do list press 2")
    print ("To move to done list press 3")
    print ("To print the done list press 4")
    print ("|*****************************|")
 

    x = input("Select a number : ")
    x = int(x)
    
    if x == 1 : 
        item = input ("Enter new item : ")
        toDoList.append(item)
    
    elif x == 2 : 
        print("  To do list : ")
        counter = 0 
        for i in toDoList :
            counter = int(counter)
            counter += 1 
            out = "   "+ str(counter)  + " - " + i 
            print (out)
        
    elif x == 3 :
        item = input ("Enter item to be moved to done list : ")
        toDoList.remove(item)
        doneList.append(item)
    
    elif x == 4 :
        print("  Done list : ")
        counter = 0
        for i in doneList :
            counter = int(counter)
            counter += 1 
            out = "   "+ str(counter)  + " - " + i 
            print (out)
    
    print ("|*****************************|")    
        