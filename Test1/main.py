import pandas as pd

agricultura = pd.read_csv('Test1/dataIN/Agricultura.csv')
pop_localitati = pd.read_csv('Test1/dataIN/PopulatieLocalitati.csv')

# print(agricultura.shape[0])
# columns = agricultura.columns[0:2].to_list() + ['Total']
# results = []
# for i in range(agricultura.shape[0]):
#    total = agricultura.iloc[i, 2:].sum()
#    results.append(list(agricultura.iloc[i,0:2]) + [total])

# cerinta1 = pd.DataFrame(results, columns=columns)
# cerinta1.to_csv('Test1/dataOUT/cerinta1.csv', index=False)

# columns = agricultura.columns[0:2].to_list() + ['Activitate']
# results = []
# for i in range(agricultura.shape[0]):
#     max = agricultura.iloc[i,2:].max()
#     nume_coloana = agricultura.iloc[i][agricultura.iloc[i] == max].index[0]
    
#     results.append(list(agricultura.iloc[i,0:2]) + [nume_coloana])

# cerinta2 = pd.DataFrame(results, columns=columns)
# cerinta2.to_csv('Test1/dataOUT/cerinta2.csv',index=False)

columns3 = [pop_localitati.columns[2]] + agricultura.columns[2:].to_list()
result3 = []
for i in range(agricultura.shape[0]):
    siruta = agricultura.iloc[i,0]

df3 = pd.DataFrame(result3, columns=columns3)
df3.to_csv('Test1/dataOUT/cer3.csv', index=False)

    

    

   

       





