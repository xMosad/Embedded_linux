file = open ("int.c" , "a")
file.write("void init_porta(void)\n")
file.write("{\n")
file.write("\tDDRA = 0b")

i = 0 
while i < 9 : 
    print ("Enter bit" , i)
    str_in = input ()
    if str_in == "in" :
        file.write("0")
        i += 1 
    
    elif str_in == "out" :
        file.write("1")
        i += 1
    
    else :
        print ("error")


file.write(";\n}") 
file.close()       
