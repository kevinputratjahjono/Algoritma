# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 19:03:30 2021

@author: kevin putra tjahjono
NIM: 065.002.100.020
"""

import math

nilai1 = int(input("Masukan Nilai A = "))
nilai2 = int(input("Masukan Nilai B = "))
nilai3 = int(input("Masukan Nilai C = "))
    
if nilai1 == 0:
        print("Bukan merupakan Persamaan Kuadrat") 

else:    
    D = (nilai2**2) - (4*nilai1*nilai3)
    
    if D > 0:
    
      x1 = (-nilai2 + math.sqrt(D)) / (2*nilai1)
      x2 = (-nilai2 - math.sqrt(D)) / (2*nilai1)
      print("Persamaan kuadrat ", nilai1, "x^2", "+", nilai2, "x", "+", (nilai3))
      print("Determinan = ", D)
      print("Akar x1 = ", x1)
      print("Akar x2 = ", x2)
      print("Dua akar berbeda")
      
    elif D == 0:
        
      x1 = (-nilai2 + math.sqrt(D)) / (2*nilai1)
      x2 = (-nilai2 - math.sqrt(D)) / (2*nilai1)
      print("Persamaan kuadrat ", nilai1, "x^2", "+", nilai2, "x", "+", (nilai3))
      print("Determinan = ", D)
      print("Akar = ", x1 or x2)
      print("Dua akar sama")
        
    elif D < 0:
        
      print("Persamaan kuadrat ", nilai1, "x^2", "+", nilai2, "x", "+", (nilai3))
      print("Determinan = ", D)
      print("Akar x1 = -", (nilai2), "+ √",(D), "/ 2*", (nilai1))
      print("Akar x2 = -", (nilai2), "- √",(D), "/ 2*", (nilai1))
      print("Tidak punya akar")


    
   

