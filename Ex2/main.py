import pandas as pd
import numpy as np

def cerinta1(educatie:pd.DataFrame):
    educatie_ponderata = educatie.apply(func = lambda x: x/x.sum(), axis = 1)
    cerinta1 = educatie_ponderata[['PersoaneAnalfabete']].sort_values(by="PersoaneAnalfabete", ascending=False)
    cerinta1.to_csv('Ex2/dataOUT/cerinta1.csv')

educatie = pd.read_csv('Ex2/dataIN/Educatie.csv', index_col=0)
#index_col = 0, specifies that the last column should be used as an index.
populatieJudete = pd.read_csv('Ex2/dataIN/PopulatieJudete.csv', index_col=0)
cerinta1(educatie)