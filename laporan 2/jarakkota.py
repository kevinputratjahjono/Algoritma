# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:19:49 2021

@author: kevin putra tjahjono
NIM: 065.002.100.020
"""

from math import sin, cos, sqrt, atan2, radians

#radius bumi
R = 6373.0 #km

lat1 = radians(float(input("masukan lattitude kota pertama = ")))
lon1 = radians(float(input("masukan longitude kota pertama = ")))
lat2 = radians(float(input("masukan lattitude kota kedua = ")))
lon2 = radians(float(input("masukan longitude kota kedua = ")))

dlon = lon2 - lon1
dlat = lat2 - lat1

#rumus
a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

#hasil
distance = R * c

print("Jarak antara dua kota adalah ", distance, "km")

