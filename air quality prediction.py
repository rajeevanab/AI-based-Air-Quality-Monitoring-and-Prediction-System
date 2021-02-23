import pandas as pd
import numpy as np
sn1 = pd.read_csv("record.csv")

sn1
sn1['ppm'].min()
sn1['ppm'].max()
data =  [[50, 'Normal'], [40, 'Normal'], [45, 'Normal']] 
  
sn2 =  pd.DataFrame(data,columns = ['ppm','air_quality'])
sn2
idx = 0
ppm = 51

for j in range(201):
        
        air_quality = "Abnormal"
        sn2.loc[idx] = [ppm,air_quality]
        idx+=1
        ppm+=1

sn2
sn1 = sn1.append(sn2, ignore_index=True)
sn1
sn1 = sn1.sample(frac = 1)
sn1.head(20)
sn1['air_quality'].value_counts()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
sn1['air_quality'] = le.fit_transform(sn1['air_quality'])
#[1 = Normal,0 = Abnormal]

sn1.head(20)
from sklearn.model_selection import train_test_split

X = sn1.drop(columns=['air_quality'])
Y = sn1['air_quality']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30)
x_train
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
# model training
model.fit(x_train, y_train)
# print metric to get performance
print("Accuracy: ",model.score(x_test, y_test) * 100)
y_pred = model.predict(x_test)
inverted = list(le.inverse_transform(y_pred[0:5]))
#print(y_pred[0:5])
inverted

#[1 = Normal,0 = Abnormal]
x_test[0:10]

#PREDICTING FOR A NEW VALUE NORMAL/ABNORMAL AIR QUALITY
new_xtest = [[6]]
new_pred =  model.predict(new_xtest)
new_inverted = list(le.inverse_transform(new_pred))
print('predicted air quality:')
print(new_inverted)
