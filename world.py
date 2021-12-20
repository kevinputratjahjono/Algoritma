# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:12:32 2021

@author: vinix
"""

import pandas as pd
df = pd.read_csv(r'D:\ZCODING\percobaan\Negara.csv')


rata = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()


def file(isi, sort):
    f = open("world.csv", 'w')
    f.write(isi)
    f.write(sort)
    f.close()

isi = 'DATA NEGARA, BENUA, SEMUANYA DAH LENGKAP\n{}\n=========================================================\n'.format(df)
sort = '{}\n=========================================================\n{}'.format(rata, std)

file(isi, sort)