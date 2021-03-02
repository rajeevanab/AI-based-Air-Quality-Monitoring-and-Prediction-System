# importing all liraries
import serial
import csv # import the csv
import time
import pandas as pd # for the dataframe
ser = serial.Serial('COM3',9600) #reading the port from the arduino
data =[]  # declare the variables
Strings =[] # declare the variables
for i in range(100): # for write the 100 values in the dataframe
    b = ser.readline() #read the data from port          
    string_n = b.decode()  # decode the data
    string = string_n.rstrip()    # parse the data     
    print(string)
    fields = ['ppm','air_quality']   # feilds for writing the data
  
# name of csv file 
filename = "record.csv"
  
# writing to csv file 
with open(filename, 'w') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = fields)  #write the header fields
    writer.writeheader()  
    samples =100 # we take 100 samples for data frame
    line = 1
    while line <= samples:
        writer.writerow({'ppm':string,'air_quality':'normal'}) #increment the  row index and write the row
        line=line+1 
        
ser.close() # close the port 
df = pd.read_csv("record.csv") # open the csv file 

df.isnull().sum() # finding the null values and sum of null values 
modifiedDF = df.dropna() # drop the null value colomns
 
modifiedDF.to_csv('record.csv',index=False) #save  the  updated data frame as csv file
