# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 09:21:09 2021

@author: vinix
"""

import pandas as pd
df = pd.read_csv(r'D:\ZCODING\percobaan\Negara.csv')


rata = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()


print('DATA NEGARA, BENUA, SEMUANYA DAH LENGKAP')
print(df)
print('=========================================================')
print(rata)
print('=========================================================')
print(std)
