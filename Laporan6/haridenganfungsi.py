# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 20:32:11 2021

@author: kevin putra tjahjono
NIM: 065.002.100.020
"""

hitung = 0
jawab = "ya"


while(jawab == "ya"):
    inputbulan = int(input("masukan bulan nya: "))
    inputtahun = int(input("masukan tahun nya: "))
    jawab = str(input("confirm? : "))

    
       
    def hitung_bulan():
    
      if(inputbulan >= 13 or inputbulan <= 0):
          print("INVALID data")
          
      elif(inputbulan == 1  or inputbulan == 3 or inputbulan == 5 
           or inputbulan == 7 or inputbulan == 8 
           or inputbulan == 10 or inputbulan == 12):
    	     print("Hari = 31")
          
      
           
      elif (inputbulan == 2):
      
        if(inputtahun % 4 == 0 and inputbulan == 2):
          print("Hari = 29")
          return
        
        else :
            print("Hari = 28")
            
      else:
          print("Hari = 30")
        
          
    hitung_bulan()