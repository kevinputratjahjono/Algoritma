# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 09:18:37 2021

@author: kevin putra tjahjono
NIM: 065.002.100.020
"""

bulan = ''

while (bulan != -1):
    print("masukan -1 jika ingin menghentikan program")
    bulan = int(input("masukan bulan(1-12): "))
    
    
    if (bulan == 1):
        hari = 31
        print("jumlah hari = ", hari)
    elif(bulan == 2):
        tahun = int(input("masukan tahun(e.g., 2021): "))
        if((tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0):
            hari = 29
            print("jumlah hari = ", hari)
        else:
            hari = 28
            print("jumlah hari = ", hari)
    elif(bulan == 3):
        hari = 31
        print("jumlah hari = ", hari)
    elif(bulan == 4):
        hari = 30
        print("jumlah hari = ", hari)
    elif(bulan == 5):
        hari = 31
        print("jumlah hari = ", hari)
    elif(bulan == 6):
        hari = 30
        print("jumlah hari = ", hari)
    elif(bulan == 7):
        hari = 31
        print("jumlah hari = ", hari)
    elif(bulan == 8):
        hari = 31
        print("jumlah hari = ", hari)
    elif(bulan == 9):
        hari = 30
        print("jumlah hari = ", hari)
    elif(bulan == 10):
        hari = 31
        print("jumlah hari = ", hari)
    elif(bulan == 11):
        hari = 30
        print("jumlah hari = ", hari)
    elif(bulan == 12):
        hari = 31
        print("jumlah hari = ", hari)
    else:
        if bulan != (1, 2, 3, 4, 5, 6, 7, 8, 9,
                     10, 11, 12):
            print("invalid data")
           
    
    
    