import streamlit as st
import numpy as np
import pandas as pd

st.title('Welcomo to the Streamlit of Trascender Global')
st.write("Hello there! Are you ready to test our model for predict a human movement, this model was train in IBM-AutoAI. You can read our blog post, where we describe all process to train it.")


#%% PLOT Signal
st.write("Remember, this is a EMG signal.")

Sx = open("D:\OneDrive - Trascender Global\EMG-project\movimientos\Movimiento4AV.txt", "r").read()
lines2 = Sx.split('\n')

sx1 = []
sx2 = []
sx3 = []
sx4 = []

# Ciclo while para leer los datos del txt, donde se aseguran que se reciban los 4 datos de la señal,
# sino es asi se salta el dato erroneo
i = 0
while i < len(lines2):
    if i == len(lines2):
        i = len(lines2) * 100
        break
    da = lines2[i]

    if len(da)>7:
        d1, d2, d3, d4 = da.split(",")

        if (len(d1)>0) and (len(d2)>0) and (len(d3)>0) and (len(d4)>0):
            sx1.append(d1)
            sx2.append(d2)
            sx3.append(d3)
            sx4.append(d4)
            i = i + 1
    else:
        i = i + 1
# Variables que son transformadas de listas a array para realizar procesos matematicos
SX1 = np.array(sx1).astype(np.float)  # Señal del canal1
SX2 = np.array(sx2).astype(np.float)  # Señal del canal 2
SX3 = np.array(sx3).astype(np.float)  # Señal del canal 3
SX4 = np.array(sx4).astype(np.float)  # Señal del canal 4

chart_data = pd.DataFrame(     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(SX1)

#%% PREDICTION
st.write("Now, predict with the csv file. You can choose a trascender signal and predict what movement was doing!")

