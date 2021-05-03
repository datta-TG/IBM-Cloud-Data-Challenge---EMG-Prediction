import streamlit as st
import numpy as np
import pandas as pd
st.title('IBM Cloud Data Challenge - Hand Movement Prediction using EMG')
st.write('Welcome to the Streamlit of Trascender Global')
st.write("Hello there! Are you ready to test our model to predict a human movement? This model was trained in IBM's AutoAI tool. You can read our blog post here: , where we describe all the process and research we had to do.")


st.write("You can read our blog post here: https://blog.trascenderglobal.com/how-we-use-ibms-watson-autoai-to-classify-a-human-hand-movement-with-emg-signals-c87d24ea276c ")
st.write("where we describe all the process and research we had to do.")

st.write("Below are our EMG signals so you can get familiar with them 😉.")

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
    
SX1 = read_txt('Movimiento1AV.txt')
SX2 = read_txt('Movimiento2AV.txt')
SX3 = read_txt('Movimiento3AV.txt')
SX4 = read_txt('Movimiento4AV.txt')

chart_data = pd.DataFrame(list(zip(SX1, SX2,SX3, SX4)),columns=['Movement 1', 'Movement 2', 'Movement 3', 'Movement 4'])

st.line_chart(chart_data)


#%%SELECT SIGNAL TO PREDICT

st.write("Now, you can predict with the CSV file. There was no time for us to let you upload it, but you can visualize it in the table below.You can then choose a Trascender Global team member signal/real movement and see what the AutoAI model prediction is!")

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
print(option)
selected_rows = data.loc[option]
st.write('### Selected Rows', selected_rows)




df=pd.read_csv("trascenderglobal-testing-EMG.csv")
lista=[]


#df['DataFrame Column'] = df['DataFrame Column'].astype(float)

for column in df.columns[:1:-1]:
	#print(column)
    #camisa=65
   # print(column)
    df[column]=df[column].astype(float)
	#print("hola")
	
#print(type(df.X1[0]))

#print(df.columns[:1:-1])
p=0
lista=[]
NC=option
for column in df.columns[:1:-1]:
     #print(df[column][NC])
    # print(p)
     p=p+1
     lista.append(df[column][NC])

 #   print(df[column].values)
#    pase=df[column].values
	#pase= (pase)
#    lista.append(pase)
	#print()
lista.reverse()
#print(lista)





# lista2= []
# for i in lista:
#     #print(i[0])
#     lista2.append(i[0])
# #	print(type())
# lista2.reverse()

# array_of_values_to_be_scored=lista2

# print(lista2)

array_of_input_fields=[
				"X1",
				"X2",
				"X3",
				"X4",
				"X5",
				"X6",
				"X7",
				"X8",
				"X9",
				"X10",
				"X11",
				"X12",
				"X13",
				"X14",
				"X15",
				"X16",
				"X17",
				"X18",
				"X19",
				"X20",
				"X21",
				"X22",
				"X23",
				"X24",
				"X25",
				"X26",
				"X27",
				"X28",
				"X29",
				"X30",
				"X31",
				"X32",
				"X33",
				"X34",
				"X35",
				"X36",
				"X37",
				"X38",
				"X39",
				"X40",
				"X41",
				"X42",
				"X43",
				"X44",
				"X45",
				"X46",
				"X47",
				"X48",
				"X49",
				"X50",
				"X51",
				"X52",
				"X53",
				"X54",
				"X55",
				"X56",
				"X57",
				"X58",
				"X59",
				"X60",
				"X61",
				"X62",
				"X63",
				"X64",
				"X65",
				"X66",
				"X67",
				"X68",
				"X69",
				"X70",
				"X71",
				"X72",
				"X73",
				"X74",
				"X75",
				"X76",
				"X77",
				"X78",
				"X79",
				"X80",
				"X81",
				"X82",
				"X83",
				"X84",
				"X85",
				"X86",
				"X87",
				"X88",
				"X89",
				"X90",
				"X91",
				"X92",
				"X93",
				"X94",
				"X95",
				"X96",
				"X97",
				"X98",
				"X99",
				"X100",
				"X101",
				"X102",
				"X103",
				"X104",
				"X105",
				"X106",
				"X107",
				"X108",
				"X109",
				"X110",
				"X111",
				"X112",
				"X113",
				"X114",
				"X115",
				"X116",
				"X117",
				"X118",
				"X119",
				"X120",
				"X121",
				"X122",
				"X123",
				"X124",
				"X125",
				"X126",
				"X127",
				"X128",
				"X129",
				"X130",
				"X131",
				"X132",
				"X133",
				"X134",
				"X135",
				"X136",
				"X137",
				"X138",
				"X139",
				"X140",
				"X141",
				"X142",
				"X143",
				"X144",
				"X145",
				"X146",
				"X147",
				"X148",
				"X149",
				"X150",
				"X151",
				"X152",
				"X153",
				"X154",
				"X155",
				"X156",
				"X157",
				"X158",
				"X159"
			]

# #array_of_input_fields=array_of_input_fields.tolist()
# print(type(array_of_input_fields[0]))
# #array_of_values_to_be_scored
array_of_values_to_be_scored=lista
import requests
#a.tolist()
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "API"

token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/7c9c375a-d4c9-49d8-ba7e-6646699a0bbe/predictions?version=2021-05-02', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
#print("Scoring response")
#print(response_scoring.json())

#print(response_scoring.json()['predictions'][0]['values'][0][0])

st.write(df['team member'][option]+" movements prediction was")
st.write(response_scoring.json()['predictions'][0]['values'][0][0])




