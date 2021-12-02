# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:31:44 2021

@author: vinix
"""

def buat(x):
    f = open(x, 'w')
    f.write(text)
    f.close()
    
def edit(x):
    f = open(x, 'a')
    print('Gunakan Enter untuk berhenti. .')
    F = False
    while (not F):       
        isi = input('isi: ')
        if isi == '':
            F = True
        else:
            f.write('{}\n'. format(isi))
        
    f.close()
    
x = input("Nama File + Format: ")
text = ('')
while x != '':
    pilih = input('Pilih: \n 1.Buat\n 2.Tulis\n 3.Selesai\n')
    #create
    if pilih == '1':    
        buat(x)
    elif pilih == '2':
        edit(x)
    elif pilih == '3':
        break
        
    else:
        ('gagal')

