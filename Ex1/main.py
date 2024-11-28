import pandas as pd
import numpy as np

def cerinta1(ro_nuts, energLoc):
    columns = [energLoc.columns[0]] + ['CoefLocalizare']
    results = []
    for i in range(energLoc.shape[0]):
        coef = np.round(energLoc.iloc[i, 1:].sum() / 8,2)
        judet = energLoc.iloc[i,0]
        results.append([judet, coef])
    cerinta1 = pd.DataFrame(results, columns=columns)
    cerinta1.to_csv('Ex1/dataOUT/cerinta1.csv',index=False)   


def cerinta2(energLoc):
    columns = energLoc.columns.to_list()
    results=[]
    for i in range(energLoc.shape[0]):
        if energLoc.iloc[i,1] > 1:
            results.append(energLoc.iloc[i,0:].to_list())
    cerinta2 = pd.DataFrame(results, columns=columns)
    cerinta2.to_csv('Ex1/dataOUT/cerinta2.csv', index=False)

def cerinta3(energloc):
    columns = [energLoc.columns[0]] + ['ActivitateDominanta']
    results=[]
    for i in range(energLoc.shape[0]):
        max = energLoc.iloc[i,1:].max()
        activitatea_max = energLoc.iloc[i,1:].idxmax() # coloana cu valoarea maxima
        results.append([energLoc.iloc[i,0], activitatea_max])
    cerinta3 = pd.DataFrame(results, columns=columns)
    cerinta3.to_csv('Ex1/dataOUT/cerinta3.csv', index=False)

def cerinta4(ro_nuts, energLoc):
    columns = ['Regiune'] + energLoc.columns[1:].to_list()
    results1 = []
    for i in range(ro_nuts.shape[0]):
        judet = ro_nuts.iloc[i,0]
        coefs = energLoc.loc[energLoc['Judet'] == judet, 'c3511':].values.flatten()
        
        regiunea = ro_nuts.iloc[i,2]
        # print(f"Processing: Judet={judet}, Regiune={regiunea}")
        # print(f"Coefficients for {judet}: {coefs}")
        results1.append([regiunea] + coefs.tolist())
    df1 = pd.DataFrame(results1, columns=columns)
    columns_to_be_summed = df1.columns[1:]
    cerinta4 = df1.groupby('Regiune')[columns_to_be_summed].mean().round(4).reset_index()
    # If the DataFrame has a custom index (e.g., after a groupby operation), reset_index() moves it into the DataFrame as a regular column.
    cerinta4.to_csv('Ex1/dataOUT/cerinta4.csv', index = False)

def cerinta5(t:pd.DataFrame):
    x = t.values
    max_indexes = np.argmax(x,axis=0)
    max_columns = t.index[max_indexes]
    print(pd.Series(max_columns, t.columns))
    return pd.Series(max_columns, t.columns)


ro_nuts = pd.read_csv('Ex1/dataIN/RO_NUTS.csv')
energLoc = pd.read_csv('Ex1/dataIN/EnergLoc.csv')

energLoc_ = energLoc.merge(ro_nuts["Regiune"],left_index=True, right_index=True)
cerinta5_ = energLoc_.groupby(by="Regiune").apply(func = cerinta5)
#del cerinta5_[cerinta5_.columns[-1]] #am sters ultima coloana
cerinta5_.to_csv("Ex1/dataOUT/Cerinta5.csv")
print(energLoc_)
