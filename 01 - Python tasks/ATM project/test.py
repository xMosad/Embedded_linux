
import data_handling 

'''
m = {}
m = data.get_data()
print(m)
data.save_data(m)
'''
f = open('current_user.txt', 'r')
print (f.read())
'''
import pandas as pd

df = pd.read_csv('ATM_data.csv')
print(df.xs(0)['id'])
loc = df.loc[df['id'] == 203659302214]
print(loc.tolist())





import csv
reader = csv.reader(open('ATM_data.csv', 'r'))
data = {}
for line in reader:
    data[line[0]]={'Name':line[1],'pass':line[2],'balance':line[3] ,'state':line[4] }
 


f = open('ATM_data.csv', 'w')
for row in data :
    temp = row+','+data[row]['Name']+','+data[row]['pass']+','+data[row]['balance']+','+data[row]['state'] +"\n"
    f.write(temp)
'''

'''
writer = csv.writer(open('ATM_data.csv', 'w'))
writer.writerows(reader)
'''
'''
id,name,pass,balance,state
215321701332,Ahmed Abdelrazek Mohamed,1783,3500166,N
203659302214,Salma Mohamed Foaad,1390,520001,N
126355700193,Adel Khaled Abdelrahman,1214,111000,N
201455998011,Saeed Amin Elsawy,2001,1200,N
201122369851,Amir Salama Elgendy,8935,178933,N
201356788002,Wael Mohamed khairy,3420,55000,N
203366789564,Mina Sameh Bishoy,1179,18000,N
201236787812,Omnia Ahmed Awad,1430,180350,N
'''
