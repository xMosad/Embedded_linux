import csv


def get_data () :
    reader = csv.reader(open('ATM_data.csv', 'r'))
    data = {}
    for line in reader:
        data[line[0]]={'Name':line[1],'pass':line[2],'balance':line[3] ,'state':line[4] }
    return data
    
    
def save_data(data) :
    f = open('ATM_data.csv', 'w')
    for row in data :
        temp = row+','+data[row]['Name']+','+data[row]['pass']+','+data[row]['balance']+','+data[row]['state'] +"\n"
        f.write(temp)
    f.close()
    
def set_userID(_id) :
    f = open('current_user.txt', 'w')
    f.write(_id)
    f.close()
    
def get_userID() :
    f = open('current_user.txt', 'r')
    text = f.read()
    f.close()
    return text