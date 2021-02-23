import serial
import csv
import time
import pandas as pd
ser = serial.Serial('COM3',9600)
data =[]
Strings =[]
for i in range(100):
    b = ser.readline()         
    string_n = b.decode()   
    string = string_n.rstrip()         
    print(string)
    fields = ['ppm','air_quality'] 
  
# name of csv file 
filename = "record.csv"
  
# writing to csv file 
with open(filename, 'w') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = fields)  
    writer.writeheader()  
    samples =100
    line = 1
    while line <= samples:
        writer.writerow({'ppm':string,'air_quality':'normal'})
        line=line+1
        
ser.close()
df = pd.read_csv("record.csv")

df.isnull().sum()
modifiedDF = df.dropna()
 
modifiedDF.to_csv('record.csv',index=False)
