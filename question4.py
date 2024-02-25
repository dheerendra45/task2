import numpy as np

def readfile(file_path):
    matrix = np.loadtxt(r"C:\Users\dheer\OneDrive\Documents\Desktop\file\chapter1.txt")
    return matrix

def transpose(matrix):
    transposed_matrix = np.transpose(matrix)
    return transposed_matrix
file_path = r"C:\Users\dheer\OneDrive\Documents\Desktop\file\chapter1.txt"
try:
    matrix = readfile(file_path)
    print("Original Matrix:")
    print(matrix)
    transposed_matrix = transpose(matrix)
    print("\nTransposed Matrix:")
    print(transposed_matrix)
except Exception as e:
    print("An error occurred:", e)
