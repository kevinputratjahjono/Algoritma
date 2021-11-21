# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 00:01:12 2021

@author: vinix
"""

def pangkat(x,y):
   if y == 0:
      return 1
   else:
      return x * pangkat(x,y-1)

x = int(input("Masukan Nilai Angka : "))
y = int(input("Masukan Nilai Pangkat : "))

print("%d dipangkatkan %d = %d" % (x,y,pangkat(x,y)))