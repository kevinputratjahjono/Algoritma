# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:50:57 2021

@author: vinix
"""

def pjumlah(angka=0, jumlah=0, i=1):
    if(jumlah<=0):
        return 0
    else:
        angka=int(input("masukan bil ke-"+str(i)+":"))
        if (jumlah==1):
            return angka
        else:
              i+=1
              return angka+pjumlah (angka,jumlah-1,i)
       
        
tot=int(input("piro: "))
nilai=pjumlah(jumlah=tot)
print("hasil: " + str(nilai))