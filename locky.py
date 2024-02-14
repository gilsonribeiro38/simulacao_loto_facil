import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import sys
from openpyxl import Workbook
from openpyxl import load_workbook
import os
import joblib
import time
import csv
datos=[]
# Carregar os dados dos jogos anteriores da lotofacil
if not os.path.exists('C:\\Lotery\\resultados\\loteria'):
    os.makedirs('C:\\Lotery\\resultados\\loteria')

wb = load_workbook('C:\\Lotery\\resultados\\loteria\\LOTO_FACIL_BY_CHAT_GPT.xlsx')
ws = wb.active

data = pd.read_csv('C:\\Lotery\\csv\\chat_gpt.csv')

# Criar uma coluna para cada número, indicando se ele foi sorteado (1) ou não (0)
for num in range(1, 26):
    try:
        data[f"num_{num}"] = data["numbers"].apply(lambda x: 1 if str(num) in x.split() else 0)
    except:
        print("NON")
# Criar as features e as labels
#features = data.drop(["numbers", "date"], axis=1)
features = data.drop(["date", "numbers"], axis=1)
labels = data["numbers"]

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=70, random_state=0)#test_size=0.2

# Treinar o modelo de regressão logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Treinar o modelo de floresta aleatória
model2 = RandomForestClassifier()
model2.fit(X_train, y_train)

# Fazer as previsões com os dados de teste
y_pred_lr = model.predict(X_test)
y_pred_rf = model2.predict(X_test)

# Calcular a precisão dos modelos
acc_lr = accuracy_score(y_test, y_pred_lr)
acc_rf = accuracy_score(y_test, y_pred_rf)

# Escolher o modelo com a maior precisão
if acc_lr > acc_rf:
    final_model = mode
    print("Mode 1: " + str(final_model()))
else:
    final_model = model2
    print("mode 2: " + str(final_model))
for i in range(15):
    print("Generation {}".format(i))
    # Gerar as previsões para 15 números
    predicted_numbers = final_model.predict(np.random.rand(1, 25))[0]
    joblib.dump(predicted_numbers, 'C:\\Lotery\\resultados\\seq_{}'.format(i)+'.sav')
    print("Números previstos:", predicted_numbers)
    datos.append(["01-01-9999",predicted_numbers])
    ws.append(datos[i])
    wb.save("C:\\Lotery\\resultados\\loteria\\LOTO_FACIL_BY_CHAT_GPT.xlsx")
    with open('C:\\Lotery\\csv\\chat_gpt.csv', 'a') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(['01-01-9999',predicted_numbers])
time.sleep(3)
os.system(r"py C:/Lotery/app.py")
