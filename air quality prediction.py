#impoerting all libraries
import pandas as pd # for data frame
import numpy as np  # for array conversions
from tkinter import *  # for ui
from PIL import Image, ImageTk
import time
value=[1] # subsititute the array value

root = Tk() # creating a tkinter window
root.wm_title("Air Quality prediction")  # make the window tittle as "Air Quality prediction"
root.after(3000, root.destroy) # adjusting timer to destroy the window
root.geometry("891x555") # adjust the size of the window as 891*555
load = Image.open("predict.jpg") #call an image file for the background ot the window
render = ImageTk.PhotoImage(load) #read the image file 
img = Label(root, image=render)   #label the image file on the tkinter window
img.image = render  
img.place(x=0, y=0)  #place the image in the tkinter window at x and y cordinates at 0
root.mainloop()     #viewing the window

sn1 = pd.read_csv("record.csv") #loading the csv file using pandas library
sn1 # view the dataframe
sn1['ppm'].min() # view the minimum value in the ppm colmn
sn1['ppm'].max() # view the maximum value in the ppm colmn
data =  [[50, 'Normal'], [40, 'Normal'], [45, 'Normal']] 
  #seting the values above is in normal condition
sn2 =  pd.DataFrame(data,columns = ['ppm','air_quality']) # set the colmns header as ppm and air quality
sn2     # view the updated data frame
idx = 0 #set the index value is 0
ppm = 51 #setting  the abnormal dataframe  

for j in range(201):
        # updating the dataframe to abnormal values with a range of 51-200 
        air_quality = "Abnormal" # update the column  air_quality
        sn2.loc[idx] = [ppm,air_quality] # put the values in the data frame 
        idx+=1 # increment the index value 
        ppm+=1 # increment the ppm value 

sn2 # view the updated data frame
sn1 = sn1.append(sn2, ignore_index=True) # merge the new data frame with  the new data frame
sn1 # view the orginal data frame 
sn1 = sn1.sample(frac = 1)
sn1.head(20) # view the orginal dataframe  with first 20 values
sn1['air_quality'].value_counts() #count the total value in the Air_quality colomn

from sklearn.preprocessing import LabelEncoder # import the label encoder library
le = LabelEncoder() #calling the label encoderfunction
sn1['air_quality'] = le.fit_transform(sn1['air_quality']) # changes the label of air_quality colomn to o's and 1's
#[1 = Normal,0 = Abnormal]

sn1.head(20) #view the dataframe  with first 20 values
from sklearn.model_selection import train_test_split 
# importing the libraries for spliting of dataframe   into test and train
X = sn1.drop(columns=['air_quality']) #Set the X values as air_quality
Y = sn1['air_quality'] #Set the Y values with respect to air_quality
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30)  #Setting the x y parameters for training 
x_train


print("LogisticRegression") #print the model name
from sklearn.linear_model import LogisticRegression # importing the library LogisticRegression
model = LogisticRegression() #loading the training model of logistic regression 
# model training
model.fit(x_train, y_train) #fit the model with x and y
# print metric to get performance
print("Accuracy: ",model.score(x_test, y_test) * 100)# print the accuracy of the trained model
y_pred = model.predict(x_test)
#predicting the y_pred value with the trained model
inverted = list(le.inverse_transform(y_pred[0:5])) # convert = the predicted values are one's and zero's to labels
#print(y_pred[0:5])
inverted #print the inverted value

#[1 = Normal,0 = Abnormal]
x_test[0:10] # input the testing values 

#PREDICTING FOR A NEW VALUE NORMAL/ABNORMAL AIR QUALITY
new_xtest = [[5]] #input the test values in specific  
new_pred =  model.predict(new_xtest) #predict the value with respect to the new xtest value
new_inverted = list(le.inverse_transform(new_pred)) # reset the label with respect the 0's and 1's 
print('predicted air quality:',str(new_inverted[0])) # print the value with remove the array function
# making air Quality UI


if new_pred == value: # if the predict value  is normal then create a tkinter window for visual interface 
        root = Tk() # creating a tkinter window
        root.wm_title("Air Quality normal") # make the window tittle as "Air Quality prediction"
        root.geometry("600x408") # adjust the size of the window as 600*408
        root.after(5000, root.destroy)# adjusting timer
        load = Image.open("open.jpg")  #call an image file for the background ot the window
        render = ImageTk.PhotoImage(load)  #read the image file 
        img = Label(root, image=render)   #label the image file on the tkinter window
        img.image = render
        img.place(x=0, y=0)   #place the image in the tkinter window at x and y cordinates at 0
        root.mainloop()      #viewing the window
else :
        root = Tk() # creating a tkinter window
        root.wm_title("Air Quality abnormal") # make the window tittle as "Air Quality prediction"
        root.geometry("600x380") # adjust the size of the window as 600*380        
        root.after(5000, root.destroy)# adjusting timer
        load = Image.open("close.jpg")  #call an image file for the background ot the window
        render = ImageTk.PhotoImage(load)  #read the image file 
        img = Label(root, image=render)    #label the image file on the tkinter window
        img.image = render
        img.place(x=0, y=0)  #place the image in the tkinter window at x and y cordinates at 0
        root.mainloop()  #viewing the window
        

        

