import pandas as pd
import numpy as np

def cerinta1(agricultura:pd.DataFrame):
    x = agricultura.apply(lambda x: x['PlantePermanente':].sum(), axis = 1)
    x.name = 'Total'
    cer1 = pd.DataFrame(agricultura.iloc[:, 0])
    sol = cer1.merge(x, left_index=True, right_index=True)
    sol.to_csv('Test1/dataOUT/cerinta1.csv')

def cerinta2(agricultura:pd.DataFrame):
    x = agricultura.apply(lambda x: x['PlantePermanente':].idxmax(), axis=1)
    x.name = 'Activitate'
    cer2 = pd.DataFrame(agricultura.iloc[:,0]).merge(x, left_index=True, right_index=True)
    cer2.to_csv('Test1/dataOUT/cerinta2.csv')

def cerinta3(agricultura:pd.DataFrame, pop:pd.DataFrame):
    x = agricultura.merge(pop[['Judet','Populatie']], left_index=True, right_index=True)
    summedCols = x.columns[1:-2].to_list()
    groupedSumm = pd.DataFrame(x.groupby(by="Judet", as_index="Judet")[summedCols].sum())
    aux = pd.DataFrame(data=pop.iloc[:,1:]).groupby(by="Judet").sum()
    cer3 = groupedSumm.merge(aux, left_index=True, right_index=True).apply(lambda x: np.round(x/x['Populatie'],2), axis=1)
    pd.DataFrame(cer3.iloc[:,0:-1]).to_csv('Test1/dataOUT/cerinta3.csv')



agricultura = pd.read_csv('Test1/dataIN/Agricultura.csv', index_col=0)
pop_localitati = pd.read_csv('Test1/dataIN/PopulatieLocalitati.csv', index_col=0)
cerinta3(agricultura, pop_localitati)