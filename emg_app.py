import streamlit as st
import numpy as np
import pandas as pd
st.title('IBM Cloud Data Challenge - Hand Movement Prediction using EMG')
st.write('Welcomo to the Streamlit of Trascender Global')
st.write("Hello there! Are you ready to test our model for predict a human movement, this model was train in IBM-AutoAI. You can read our blog post, where we describe all process to train it.")


#%% PLOT Signal
st.write("Remember, this is a EMG signal.")

def read_txt(name):
    Sx = open(name, "r").read()
    sx1 = [] #Un sensor
    # Ciclo while para leer los datos del txt, donde se aseguran que se reciban los 4 datos de la señal,
    # sino es asi se salta el dato erroneo
    i = 0
    lines2 = Sx.split('\n')
    while i < len(lines2):
        if i == len(lines2):
            i = len(lines2) * 100
            break
        da = lines2[i]

        if len(da)>7:
            d1, d2, d3, d4 = da.split(",")

            if (len(d1)>0) and (len(d2)>0) and (len(d3)>0) and (len(d4)>0):
                sx1.append(d1)
                i = i + 1
        else:
            i = i + 1
    # Variables que son transformadas de listas a array para realizar procesos matematicos
    SX1 = np.array(sx1).astype(np.float)  # Señal del canal1
    
    return SX1
    
SX1 = read_txt('movimientos\Movimiento1AV.txt')
SX2 = read_txt('movimientos\Movimiento2AV.txt')
SX3 = read_txt('movimientos\Movimiento3AV.txt')
SX4 = read_txt('movimientos\Movimiento4AV.txt')

chart_data = pd.DataFrame(list(zip(SX1, SX2,SX3, SX4)),columns=['Movement 1', 'Movement 2', 'Movement 3', 'Movement 4'])

st.line_chart(chart_data)


#%%SELECT SIGNAL TO PREDICT

st.write("Now, predict with the csv file. You can choose a trascender signal and predict what movement was doing!")

df = pd.read_csv('trascenderglobal-testing-EMG.csv')

data = df.iloc[0:12,:]
st.write('### Signals', data)

values=[]
names = data['team member'].tolist()
mov = data['label'].to_list()

for i in range(len(names)):
    values.append(f'{names[i]}- Movement {mov[i]}')

options = data.index.tolist() 
dic = dict(zip(options, values))

option = st.selectbox('Choose a signal', options, format_func=lambda x: dic[x])

selected_rows = data.loc[option]
st.write('### Selected Rows', selected_rows)

#%% PREDICTION


