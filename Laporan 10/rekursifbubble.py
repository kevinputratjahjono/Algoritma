# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:28:58 2021

@author: vinix
"""

def tukar(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
def bubbleSort(A, n):
 
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            tukar(A, i, i + 1)
 
    if n - 1 > 1:
        bubbleSort(A, n - 1)
 
 
if __name__ == '__main__':
 
    A = [5, -2, 8, 9, 4, 1, 3 ]
 
    bubbleSort(A, len(A))
 
    # print the sorted list
    print("List yang sudah di sorting\n",A)
