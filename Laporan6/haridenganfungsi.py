# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 20:32:11 2021

@author: kevin putra tjahjono
NIM: 065.002.100.020
"""

hitung = 0
jawab = "ya"


while(jawab == "ya"):
    bulan = int(input("masukan bulan nya: "))
    tahun = int(input("masukan tahun nya: "))
    jawab = str(input("confirm? : "))

    
       
    def hitung_bulan():
    
      if(bulan == 1  or bulan == 3 or bulan == 5 
           or bulan == 7 or bulan == 8 
           or bulan == 10 or bulan == 12):
    	     print("Hari = 31")

          
      elif(bulan >= 13 or bulan <= 0):
          print("INVALID data")          
      
           
      elif (bulan == 2):
      
        if(tahun % 4 == 0 and bulan == 2):
          print("Hari = 29")
          return
        
        else :
            print("Hari = 28")
            
      else:
          print("Hari = 30")
        
          
    hitung_bulan()
