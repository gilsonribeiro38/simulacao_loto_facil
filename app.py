import pandas as pd
from collections import Counter
from array import array
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import LSTM,Dense,Bidirectional,Dropout
import sys
from openpyxl import Workbook
from openpyxl import load_workbook
import os
import joblib
import pyautogui
if not os.path.exists('C:\\Lotery\\resultados\\loteria'):
    os.makedirs('C:\\Lotery\\resultados\\loteria')

wb = load_workbook('C:\\Lotery\\resultados\\loteria\\LOTO_FACIL_SIMULACAO.xlsx')
ws = wb.active

df = pd.read_csv('C:\\Lotery\\csv\\loto_facil.csv')
matrix_seq_0 = joblib.load('C:\\Lotery\\resultados\\seq_0.sav')
matrix_seq_1 = joblib.load('C:\\Lotery\\resultados\\seq_1.sav')
matrix_seq_2 = joblib.load('C:\\Lotery\\resultados\\seq_2.sav')
matrix_seq_3 = joblib.load('C:\\Lotery\\resultados\\seq_3.sav')
matrix_seq_4 = joblib.load('C:\\Lotery\\resultados\\seq_4.sav')
matrix_seq_5 = joblib.load('C:\\Lotery\\resultados\\seq_5.sav')
matrix_seq_6 = joblib.load('C:\\Lotery\\resultados\\seq_6.sav')
matrix_seq_7 = joblib.load('C:\\Lotery\\resultados\\seq_7.sav')
matrix_seq_8 = joblib.load('C:\\Lotery\\resultados\\seq_8.sav')
matrix_seq_9 = joblib.load('C:\\Lotery\\resultados\\seq_9.sav')
matrix_seq_10 = joblib.load('C:\\Lotery\\resultados\\seq_10.sav')
matrix_seq_11 = joblib.load('C:\\Lotery\\resultados\\seq_11.sav')
matrix_seq_12 = joblib.load('C:\\Lotery\\resultados\\seq_12.sav')
matrix_seq_13 = joblib.load('C:\\Lotery\\resultados\\seq_13.sav')
matrix_seq_14 = joblib.load('C:\\Lotery\\resultados\\seq_14.sav')

dados_seq_0=[]
dados_seq_0.append(matrix_seq_0.split())
a0=int(dados_seq_0[0][0])
a1=int(dados_seq_0[0][1])
a2=int(dados_seq_0[0][1])
a3=int(dados_seq_0[0][3])
a4=int(dados_seq_0[0][4])
a5=int(dados_seq_0[0][5])
a6=int(dados_seq_0[0][6])
a7=int(dados_seq_0[0][7])
a8=int(dados_seq_0[0][8])
a9=int(dados_seq_0[0][9])
a10=int(dados_seq_0[0][10])
a11=int(dados_seq_0[0][11])
a12=int(dados_seq_0[0][12])
a13=int(dados_seq_0[0][13])
a14=int(dados_seq_0[0][14])

dados_seq_1=[]
dados_seq_1.append(matrix_seq_1.split())
b0=int(dados_seq_1[0][0])
b1=int(dados_seq_1[0][1])
b2=int(dados_seq_1[0][1])
b3=int(dados_seq_1[0][3])
b4=int(dados_seq_1[0][4])
b5=int(dados_seq_1[0][5])
b6=int(dados_seq_1[0][6])
b7=int(dados_seq_1[0][7])
b8=int(dados_seq_1[0][8])
b9=int(dados_seq_1[0][9])
b10=int(dados_seq_1[0][10])
b11=int(dados_seq_1[0][11])
b12=int(dados_seq_1[0][12])
b13=int(dados_seq_1[0][13])
b14=int(dados_seq_1[0][14])

dados_seq_2=[]
dados_seq_2.append(matrix_seq_2.split())
c0=int(dados_seq_2[0][0])
c1=int(dados_seq_2[0][1])
c2=int(dados_seq_2[0][1])
c3=int(dados_seq_2[0][3])
c4=int(dados_seq_2[0][4])
c5=int(dados_seq_2[0][5])
c6=int(dados_seq_2[0][6])
c7=int(dados_seq_2[0][7])
c8=int(dados_seq_2[0][8])
c9=int(dados_seq_2[0][9])
c10=int(dados_seq_2[0][10])
c11=int(dados_seq_2[0][11])
c12=int(dados_seq_2[0][12])
c13=int(dados_seq_2[0][13])
c14=int(dados_seq_2[0][14])

dados_seq_3=[]
dados_seq_3.append(matrix_seq_3.split())
d0=int(dados_seq_3[0][0])
d1=int(dados_seq_3[0][1])
d2=int(dados_seq_3[0][1])
d3=int(dados_seq_3[0][3])
d4=int(dados_seq_3[0][4])
d5=int(dados_seq_3[0][5])
d6=int(dados_seq_3[0][6])
d7=int(dados_seq_3[0][7])
d8=int(dados_seq_3[0][8])
d9=int(dados_seq_3[0][9])
d10=int(dados_seq_3[0][10])
d11=int(dados_seq_3[0][11])
d12=int(dados_seq_3[0][12])
d13=int(dados_seq_3[0][13])
d14=int(dados_seq_3[0][14])

dados_seq_4=[]
dados_seq_4.append(matrix_seq_4.split())
e0=int(dados_seq_4[0][0])
e1=int(dados_seq_4[0][1])
e2=int(dados_seq_4[0][1])
e3=int(dados_seq_4[0][3])
e4=int(dados_seq_4[0][4])
e5=int(dados_seq_4[0][5])
e6=int(dados_seq_4[0][6])
e7=int(dados_seq_4[0][7])
e8=int(dados_seq_4[0][8])
e9=int(dados_seq_4[0][9])
e10=int(dados_seq_4[0][10])
e11=int(dados_seq_4[0][11])
e12=int(dados_seq_4[0][12])
e13=int(dados_seq_4[0][13])
e14=int(dados_seq_4[0][14])

dados_seq_5=[]
dados_seq_5.append(matrix_seq_5.split())
f0=int(dados_seq_5[0][0])
f1=int(dados_seq_5[0][1])
f2=int(dados_seq_5[0][1])
f3=int(dados_seq_5[0][3])
f4=int(dados_seq_5[0][4])
f5=int(dados_seq_5[0][5])
f6=int(dados_seq_5[0][6])
f7=int(dados_seq_5[0][7])
f8=int(dados_seq_5[0][8])
f9=int(dados_seq_5[0][9])
f10=int(dados_seq_5[0][10])
f11=int(dados_seq_5[0][11])
f12=int(dados_seq_5[0][12])
f13=int(dados_seq_5[0][13])
f14=int(dados_seq_5[0][14])

dados_seq_6=[]
dados_seq_6.append(matrix_seq_6.split())
g0=int(dados_seq_6[0][0])
g1=int(dados_seq_6[0][1])
g2=int(dados_seq_6[0][1])
g3=int(dados_seq_6[0][3])
g4=int(dados_seq_6[0][4])
g5=int(dados_seq_6[0][5])
g6=int(dados_seq_6[0][6])
g7=int(dados_seq_6[0][7])
g8=int(dados_seq_6[0][8])
g9=int(dados_seq_6[0][9])
g10=int(dados_seq_6[0][10])
g11=int(dados_seq_6[0][11])
g12=int(dados_seq_6[0][12])
g13=int(dados_seq_6[0][13])
g14=int(dados_seq_6[0][14])

dados_seq_7=[]
dados_seq_7.append(matrix_seq_7.split())
h0=int(dados_seq_7[0][0])
h1=int(dados_seq_7[0][1])
h2=int(dados_seq_7[0][1])
h3=int(dados_seq_7[0][3])
h4=int(dados_seq_7[0][4])
h5=int(dados_seq_7[0][5])
h6=int(dados_seq_7[0][6])
h7=int(dados_seq_7[0][7])
h8=int(dados_seq_7[0][8])
h9=int(dados_seq_7[0][9])
h10=int(dados_seq_7[0][10])
h11=int(dados_seq_7[0][11])
h12=int(dados_seq_7[0][12])
h13=int(dados_seq_7[0][13])
h14=int(dados_seq_7[0][14])

dados_seq_8=[]
dados_seq_8.append(matrix_seq_8.split())
i0=int(dados_seq_8[0][0])
i1=int(dados_seq_8[0][1])
i2=int(dados_seq_8[0][1])
i3=int(dados_seq_8[0][3])
i4=int(dados_seq_8[0][4])
i5=int(dados_seq_8[0][5])
i6=int(dados_seq_8[0][6])
i7=int(dados_seq_8[0][7])
i8=int(dados_seq_8[0][8])
i9=int(dados_seq_8[0][9])
i10=int(dados_seq_8[0][10])
i11=int(dados_seq_8[0][11])
i12=int(dados_seq_8[0][12])
i13=int(dados_seq_8[0][13])
i14=int(dados_seq_8[0][14])

dados_seq_9=[]
dados_seq_9.append(matrix_seq_9.split())
k0=int(dados_seq_9[0][0])
k1=int(dados_seq_9[0][1])
k2=int(dados_seq_9[0][1])
k3=int(dados_seq_9[0][3])
k4=int(dados_seq_9[0][4])
k5=int(dados_seq_9[0][5])
k6=int(dados_seq_9[0][6])
k7=int(dados_seq_9[0][7])
k8=int(dados_seq_9[0][8])
k9=int(dados_seq_9[0][9])
k10=int(dados_seq_9[0][10])
k11=int(dados_seq_9[0][11])
k12=int(dados_seq_9[0][12])
k13=int(dados_seq_9[0][13])
k14=int(dados_seq_9[0][14])

dados_seq_10=[]
dados_seq_10.append(matrix_seq_10.split())
l0=int(dados_seq_10[0][0])
l1=int(dados_seq_10[0][1])
l2=int(dados_seq_10[0][1])
l3=int(dados_seq_10[0][3])
l4=int(dados_seq_10[0][4])
l5=int(dados_seq_10[0][5])
l6=int(dados_seq_10[0][6])
l7=int(dados_seq_10[0][7])
l8=int(dados_seq_10[0][8])
l9=int(dados_seq_10[0][9])
l10=int(dados_seq_10[0][10])
l11=int(dados_seq_10[0][11])
l12=int(dados_seq_10[0][12])
l13=int(dados_seq_10[0][13])
l14=int(dados_seq_10[0][14])

dados_seq_11=[]
dados_seq_11.append(matrix_seq_11.split())
m0=int(dados_seq_11[0][0])
m1=int(dados_seq_11[0][1])
m2=int(dados_seq_11[0][1])
m3=int(dados_seq_11[0][3])
m4=int(dados_seq_11[0][4])
m5=int(dados_seq_11[0][5])
m6=int(dados_seq_11[0][6])
m7=int(dados_seq_11[0][7])
m8=int(dados_seq_11[0][8])
m9=int(dados_seq_11[0][9])
m10=int(dados_seq_11[0][10])
m11=int(dados_seq_11[0][11])
m12=int(dados_seq_11[0][12])
m13=int(dados_seq_11[0][13])
m14=int(dados_seq_11[0][14])

dados_seq_12=[]
dados_seq_12.append(matrix_seq_12.split())
n0=int(dados_seq_12[0][0])
n1=int(dados_seq_12[0][1])
n2=int(dados_seq_12[0][1])
n3=int(dados_seq_12[0][3])
n4=int(dados_seq_12[0][4])
n5=int(dados_seq_12[0][5])
n6=int(dados_seq_12[0][6])
n7=int(dados_seq_12[0][7])
n8=int(dados_seq_12[0][8])
n9=int(dados_seq_12[0][9])
n10=int(dados_seq_12[0][10])
n11=int(dados_seq_12[0][11])
n12=int(dados_seq_12[0][12])
n13=int(dados_seq_12[0][13])
n14=int(dados_seq_12[0][14])

dados_seq_13=[]
dados_seq_13.append(matrix_seq_13.split())
o0=int(dados_seq_13[0][0])
o1=int(dados_seq_13[0][1])
o2=int(dados_seq_13[0][1])
o3=int(dados_seq_13[0][3])
o4=int(dados_seq_13[0][4])
o5=int(dados_seq_13[0][5])
o6=int(dados_seq_13[0][6])
o7=int(dados_seq_13[0][7])
o8=int(dados_seq_13[0][8])
o9=int(dados_seq_13[0][9])
o10=int(dados_seq_13[0][10])
o11=int(dados_seq_13[0][11])
o12=int(dados_seq_13[0][12])
o13=int(dados_seq_13[0][13])
o14=int(dados_seq_13[0][14])

dados_seq_14=[]
dados_seq_14.append(matrix_seq_14.split())
p0=int(dados_seq_14[0][0])
p1=int(dados_seq_14[0][1])
p2=int(dados_seq_14[0][1])
p3=int(dados_seq_14[0][3])
p4=int(dados_seq_14[0][4])
p5=int(dados_seq_14[0][5])
p6=int(dados_seq_14[0][6])
p7=int(dados_seq_14[0][7])
p8=int(dados_seq_14[0][8])
p9=int(dados_seq_14[0][9])
p10=int(dados_seq_14[0][10])
p11=int(dados_seq_14[0][11])
p12=int(dados_seq_14[0][12])
p13=int(dados_seq_14[0][13])
p14=int(dados_seq_14[0][14])

#https://colab.research.google.com/drive/1TwkfU1zEDXQTl5cYzT-DaGaUuQ8Gbs2C?usp=sharing
scaler = StandardScaler().fit(df.values)
transformed_dataset = scaler.transform(df.values)
transformed_df = pd.DataFrame(data=transformed_dataset,index=df.index)

numbers_of_rows = df.values.shape[0] #all our games
window_length = 15 #amount pf past games we need  to take in concideration for prediction
number_of_features = df.values.shape[1]#balls count

#Create train dataset and labels for each row.It should have format for keras lstm model(rows,window size,balls)
train = np.empty([numbers_of_rows-window_length,window_length,number_of_features],dtype=float)
label = np.empty([numbers_of_rows-window_length,number_of_features],dtype=float)
window_lenght = 15
for i in range(0,numbers_of_rows-window_lenght):
  train[i]=transformed_df.iloc[i:i+window_lenght,0:number_of_features]
  label[i]=transformed_df.iloc[i+window_lenght:i+window_lenght+1,0:number_of_features]

batch_size = 100
model = Sequential()
model.add(Dropout(0.3))
#1
model.add(Bidirectional(LSTM(240,
                        input_shape=(window_lenght,number_of_features),
                        return_sequences=True)))
#2
model.add(Dropout(0.6))
model.add(Bidirectional(LSTM(240,
                        input_shape=(window_lenght,number_of_features),
                        return_sequences=True)))
#7
model.add(Dropout(0.9))
model.add(Bidirectional(LSTM(240,
                        input_shape=(window_lenght,number_of_features),
                        return_sequences=False)))
#model.add(Dropout(0.2))
model.add(Dense(59))
model.add(Dense(number_of_features))
model.compile(loss='mse',optimizer='rmsprop',metrics=['accuracy'])

#trainning model
model.fit(train,label,batch_size=100,epochs=36)
#Primeiro Jogo
to_predict0=np.array([ [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14],[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14],
                       [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14],[d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14],
                       [e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14],[f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14],
                       [g0,g1,g2,g3,g4,g5,g6,g7,g8,g8,g10,g11,g12,g13,g14],[h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14],
                       [i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14],[k0,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14],
                       [l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14],[m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14],
                       [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14],[o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14],
                       [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14]])

scaled_to_predict0 = scaler.transform(to_predict0)
scaled_predicted0_output_1=model.predict(np.array(np.array([scaled_to_predict0])))
print(scaler.inverse_transform(scaled_predicted0_output_1).astype(int)[0])
ws.append([str(scaler.inverse_transform(scaled_predicted0_output_1).astype(int)[0])])
wb.save("C:\\Lotery\\resultados\\loteria\\LOTO_FACIL_SIMULACAO.xlsx")

#trainning model
model.fit(train,label,batch_size=100,epochs=32)
#Segundo Jogo
to_predict1=np.array([ [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14],[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14],
                       [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14],[d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14],
                       [e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14],[f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14],
                       [g0,g1,g2,g3,g4,g5,g6,g7,g8,g8,g10,g11,g12,g13,g14],[h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14],
                       [i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14],[k0,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14],
                       [l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14],[m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14],
                       [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14],[o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14],
                       [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14]])

#trainning model
scaled_to_predict1 = scaler.transform(to_predict1)
scaled_predicted1_output_1=model.predict(np.array(np.array([scaled_to_predict1])))
print(scaler.inverse_transform(scaled_predicted2_output_1).astype(int)[0])
ws.append([str(scaler.inverse_transform(scaled_predicted1_output_1).astype(int)[0])])
wb.save("C:\\Lotery\\resultados\\loteria\\LOTO_FACIL_SIMULACAO.xlsx")

#trainning model
model.fit(train,label,batch_size=100,epochs=32)
#Terceiro jogo
to_predict2=np.array([ [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14],[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14],
                       [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14],[d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14],
                       [e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14],[f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14],
                       [g0,g1,g2,g3,g4,g5,g6,g7,g8,g8,g10,g11,g12,g13,g14],[h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14],
                       [i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14],[k0,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14],
                       [l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14],[m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14],
                       [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14],[o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14],
                       [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14]])

scaled_to_predict2 = scaler.transform(to_predict2)
scaled_predicted2_output_1=model.predict(np.array(np.array([scaled_to_predict2])))
print(scaler.inverse_transform(scaled_predicted2_output_1).astype(int)[0])
ws.append([str(scaler.inverse_transform(scaled_predicted2_output_1).astype(int)[0])])
wb.save("C:\\Lotery\\resultados\\loteria\\LOTO_FACIL_SIMULACAO.xlsx")

model.fit(train,label,batch_size=100,epochs=32)
#Quarto Jogo
to_predict3=np.array([ [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14],[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14],
                       [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14],[d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14],
                       [e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14],[f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14],
                       [g0,g1,g2,g3,g4,g5,g6,g7,g8,g8,g10,g11,g12,g13,g14],[h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14],
                       [i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14],[k0,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14],
                       [l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14],[m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14],
                       [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14],[o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14],
                       [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14]])

scaled_to_predict3 = scaler.transform(to_predict3)
scaled_predicted3_output_1=model.predict(np.array(np.array([scaled_to_predict3])))
print(scaler.inverse_transform(scaled_predicted3_output_1).astype(int)[0])
ws.append([str(scaler.inverse_transform(scaled_predicted3_output_1).astype(int)[0])])
wb.save("C:\\Lotery\\resultados\\loteria\\LOTO_FACIL_SIMULACAO.xlsx")