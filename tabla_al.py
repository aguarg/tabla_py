# Generador de una tabla de números aleatorios en formato txt, pdf o csv para imprimir.

# ÍNDICE / INDEX:
# 1- Módules / Modules.
# 2- Estado del script y opciones elegidas/ Script state and selected options.
# 3- Función limpiar la pantalla / function to clear the screen.
# 4- Función para elegir idioma / function for language selection.
# 5- Función para elegir cuántos números se van a generar / Function to specify how many numbers to generate.
# 6- Número inicial / initial number
# 7- Número final / ending number
# 8- Formato del archivo de salida / format of generated file


# 1- MÓDULOS:
# Módulo para aleatorizar:
import random   

# Módulo para manejar la consola de windows y linux creando una funcion clear(): 
from os import system, name 




# 2- Opciones y estados / options and states:
opciones = {
    "idioma": 1, #1: español, 2: english
    "cantidad_numeros": 0,
    "valor_inicio": 0,
    "valor_fin": 0,
    "formato_archivo": 0 #0: txt, 1: PDF, 2: csv

}



# 3- Función para limpiar la pantalla / Function to clear the screen:
def borrar(): 
  
    #para Windows
    if name == 'nt': 
        _ = system('cls') 
  
    #para Linux y Mac 
    else: 
        _ = system('clear')


# 4- Selector de idioma / language selector
def elegir_idioma():
    idioma = int(input("""Elija idioma / Select language: 
                            1) Para español 
                            2) For english
                            """))

    opciones["idioma"] = idioma




# 5- Elegir cuantos números generar/ select how many numbers to generate:
def elegir_cantidad_numeros():
    if opciones["idioma"] == 1:
        cantidad = int(input("¿Cuántos números desea generar?: "))

    elif opciones["idioma"] == 2:
        cantidad = int(input("How many numbers you want to generate?: "))  

    opciones["cantidad_numeros"] = cantidad      


# 6 - Elegir número inicial / select starting number:
def inicio():
    if opciones["idioma"] == 1:
        inicio = int(input("¿Cuál es el número de inicio?: "))

    elif opciones["idioma"] == 2:
        inicio = int(input("From which number start?: "))

    opciones["valor_inicio"] = inicio    
        

# 7 - Elegir número final / select ending number:
def final():
    if opciones["idioma"] == 1:
        final = int(input("¿Hasta qué número?: "))

    elif opciones["idioma"] == 2:
        final = int(input("To which number?: "))

    opciones["valor_fin"] = final


# 8 - Elegir formato del archivo de salida:
def formato_archivo():
    formato = int(input("""Elija el tipo del archivo a generar / Select the type of the file to generate: 
                            1) .txt 
                            2) .pdf
                            3) .csv
                            """))

    opciones["formato_archivo"] = formato





# Inicio del script:
print("CREADOR DE TABLA DE NÚMEROS ALEATORIOS / RANDOM NUMBERS TABLE GENERATOR")

elegir_idioma()
inicio()
final()  
elegir_cantidad_numeros()
formato_archivo()

# Esto es para ir viendo si el diccionario se va actualizando debidamente
print(opciones)  









