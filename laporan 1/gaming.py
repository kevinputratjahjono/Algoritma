# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:31:24 2021

@author: vinix
"""

print("haloo")
print("selamat pagi")
print("============")
print("dibuat oleh Kevin Putra")
print("asli seasli aslinya dari cibinong")
print("pernah sekolah di SMA sekarang kuliah di Trisakti")
print("boleh kenalan?")

x = input("your name . .")

print("==================")

print("haloo. . .", x) 
print("senang bertemu dengan mu")
print("semoga kita semakin akrab")

print("==================")

print("kamu asalnya dari mana?")

y = input("asal. . .")

print("ohh kamu dari ", y, "kalau aku dari cibinong")

print("==================")

print("kamu umurnya berapa?")

z = input("umur kamu. . ")

print("jadi umur kamu ", z, "syukurlah aku tidak akan dikejar polisi")

print("==================")

print("aku sayang kamu", x, "( ͡° ͜ʖ ͡°)")

print("==================")

print("aku sih sayang kamu. kamu?")

while True:
    choice = input("pilih(iya/tidak): ")
    
    if choice in ('iya', 'tidak' ):
        reason = input("kenapa?")
        
        if choice == 'iya':
            print("alasan kamu ", reason, "kalau begitu ayo. . .")
        
        elif choice == 'tidak':
            print("alasan kamu ", reason, "baiklah aku menerima")
            
        
        coba_lagi = input("mau coba lagi? (iya/tidak): ")
        if coba_lagi == "tidak":
            break
        
        
        
    else:
            print("pilih yang benar!!")
