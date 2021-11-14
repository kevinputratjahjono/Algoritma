# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 00:48:52 2021

@author: vinix
"""
print("Program untuk angka ordinal")

x = False

n = ""

def make_ordinal(n):

    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    print("(", n, ",", '"',suffix,'"', ")")
while (not x):
    print("Gunakan '-1' untuk menghentikan")
    n = int(input("masukan angka: ")) 
    if n == -1:
        x = True
    else:
        make_ordinal(n)

