import pandas as pd
import numpy as np

def cerinta1(educatie:pd.DataFrame):
    educatie_ponderata = educatie.apply(func = lambda x: x/x.sum(), axis = 1)
    cerinta1 = educatie_ponderata[['PersoaneAnalfabete']].sort_values(by="PersoaneAnalfabete", ascending=False)
    cerinta1.to_csv('Ex2/dataOUT/cerinta1.csv')

def cerinta2(educatie:pd.DataFrame, populatie:pd.DataFrame):
    educatie_ = educatie.copy()
    educatie_ = educatie_.merge(populatie, right_index=True, left_index=True)
    educatie_['FaraScoala_Analfabeti'] = educatie_.apply(func=lambda x: (x['FaraScoala'] + x['PersoaneAnalfabete'])*100000/x['Populatie'], axis=1)
    x = pd.DataFrame(educatie_.iloc[:, -1]).sort_values(by="FaraScoala_Analfabeti", ascending=False)
    x.to_csv('Ex2/dataOUT/cerinta2.csv')

# Să se salveze în fișierul Cerinta3.csv numărul persoanelor pe niveluri de educație la nivel de regiune. Se va 
# salva pentru fiecare regiune, numele regiunii și numărul de persoane pentru fiecare nivel de educație.
def cerinta3(educatie:pd.DataFrame, ro_nuts:pd.DataFrame):
    educatie_roNuts = educatie.merge(ro_nuts, left_index=True, right_index=True)
    summed_col = educatie.columns[0:].to_list()
    x =educatie_roNuts.groupby(by="Regiune")[summed_col].sum()
    x.to_csv('Ex2/dataOUT/cerinta3.csv')

def weights(x:pd.DataFrame):
    value = np.average(x.values[:,:-1], weights=x.values[:,-1], axis=0)
    return pd.Series(value,x.columns[:-1])


# Să se determine pentru fiecare regiune și fiecare nivel de educație județul cu ponderea cea mai mare. Se va 
# salva în fișierul Cerinta4.csv, numele regiunii și județele cu ponderile cele mai mari pe fiecare nivel de educație.
def cerinta5(educatie:pd.DataFrame, ro_nuts:pd.DataFrame, populatie:pd.DataFrame):
    ed_pop  = educatie.merge(populatie, right_index=True, left_index=True)
    ed_pop_reg = ed_pop.merge(ro_nuts['Regiune'], right_index=True, left_index=True)
    cerinta5 = ed_pop_reg.groupby(by="Regiune").apply(func=weights)
    cerinta5.to_csv('Ex2/dataOUT/cerinta5.csv')
   


educatie = pd.read_csv('Ex2/dataIN/Educatie.csv', index_col=0)
#index_col = 0, specifies that the last column should be used as an index.
populatieJudete = pd.read_csv('Ex2/dataIN/PopulatieJudete.csv', index_col=0)
ro_nuts = pd.read_csv('Ex2/dataIN/RO_NUTS.csv', index_col=0)
cerinta5(educatie,ro_nuts,populatieJudete)

