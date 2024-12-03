import pandas as pd
import numpy as np


#cerinta1
array = np.full((7,7),7,dtype=float)
np.fill_diagonal(array, 33)
array[3][3] = 77
for i in range(1,6):
   for j in range(1,6):
       array[i]
   
print(array)

#cerinta 4
def fun(numb):
    return numb * np.random.randint(0,10)
array = fun(np.random.rand(100))
row_labels = ['L_'+str(i+1) for i in range(100)]
series = pd.Series(array, index=row_labels)
# print(series)

#cerinta5
ndArray = fun(np.random.rand(11,5))
row_df = ['L_'+str(i+1) for i in range (11)]
cols_df = ['C_'+str(i+1) for i in range (5)]
df = pd.DataFrame(data=ndArray, columns=cols_df, index=row_df)
# print(df)


#cerinta6
dict = {'S_'+str(i+1) : grade for i in range (8) for grade in [np.random.randint(1,11,5)] }
df2 = pd.DataFrame(dict)
print(df2)

#cerinta7
labels = ['Ex_'+str(i+1) for i in range (5)]
grades = np.random.randint(1,11,[7,5]).tolist()
series = [pd.Series(data=grade, index=labels) for grade in grades]
dict2 = {'Stud'+str(i+1) : series[i] for i in range (7)}
df3 = pd.DataFrame(data=dict2)
#print(df3)

#cerinta9
keys1 = ['An_'+str(i+1) for i in range(5)]
keys2 = ['Stud'+str(i+1) for i in range(7)]
grades2 = np.random.randint(1,11,[7,5]).tolist()
dict3 = {keys2[i] :grades2[i] for i in range(7) }
dict4 = {keys1[i] :dict3.items() for i in range(5)}
df4 = pd.DataFrame(dict4)
print(df4)