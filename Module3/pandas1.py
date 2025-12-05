import numpy as np
import pandas as pd
dict = {"Name":["Ajay",np.nan,np.nan,np.nan],
        "Class": ["IX",np.nan,"XI","XII"],"Roll":["21",np.nan,"38","64"]}
data = pd.DataFrame(dict)
#print(data.isnull())
#bool_series1 = pd.isnull(data["Name"])
#bool_series2 = pd.isnull(data["Class"])
#bool_series3 = pd.isnull(data["Roll"])
#print(data[bool_series1])
#print(data[bool_series2])
#print(data[bool_series3])
#data.fillna(0,inplace=True)
data.dropna(how='any',inplace=True)
print(data)










'''s1 = pd.Series([39,41,42,44],index = ["A","B","C","D"])
s2 = pd.Series([10,10,10,10],index = ["A","B","D","F"])
print(s1[:2]*100)
print(s1*s2)
print(s2[ : : -1]*10)'''
