# Generador de una tabla de números aleatorios en formato txt, pdf o csv para imprimir.

# ÍNDICE / INDEX:
# 1- Módules / Modules.
# 2- Estado del script y opciones elegidas/ Script state and selected options.
# 3- Función limpiar la pantalla / function to clear the screen.
# 4- Función para elegir idioma / function for language selection.
# 5 Función para elegir cuántos números se van a generar / Function to specify how many numbers to generate.



# 1- MÓDULOS:
# Módulo para aleatorizar:
import random   

# Módulo para manejar la consola de windows y linux creando una funcion clear(): 
from os import system, name 




# 2- Opciones y estados / options and states:
opciones = {
    "idioma": 1,
    "cantidad_numeros": 0,
    "valor_inicio": 0,
    "valor_fin": 0,
    "formato_archivo": 0

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



# Inicio del script:
print("CREADOR DE TABLA DE NÚMEROS ALEATORIOS / RANDOM NUMBERS TABLE GENERATOR")

elegir_idioma()
elegir_cantidad_numeros()  

print(opciones)  









