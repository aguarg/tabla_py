# ----------------------CSV---------------------
import csv

numeros = [2, 54456, 1, 3, 67, 23423235234566256245, 2, 9934, 69, 22, 0, 67, 53, 12, 56, 34,1242, 5522, 22, 9778, 334, 3424, 747, 7, 88]

nombre_archivo = input("nombre del archivo?: ")

with open(nombre_archivo, 'w', newline="") as file:
	writer = csv.writer(file, delimiter="\t", lineterminator="\n")
    
	writer.writerow(numeros)
	
