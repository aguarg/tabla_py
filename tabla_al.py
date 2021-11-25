# Generador de una tabla de números aleatorios en formato txt, pdf o csv para imprimir.

# ÍNDICE / INDEX:
# 1- Módules / Modules.
# 2- Estado del script y opciones elegidas/ Script state and selected options.
# 3- Función limpiar la pantalla / clear screen function.



# 1- MÓDULOS:
# Módulo para aleatorizar:
import random   

# Módulo para manejar la consola de windows y linux creando una funcion clear(): 
from os import system, name 




# 2- Opciones y estados / options and states:
opciones = {
    "idioma": 0,
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





print("CREADOR DE TABLA DE NÚMEROS ALEATORIOS / RANDOM NUMBERS TABLE GENERATOR")


# Selector de idioma / language selector
idioma = int(input("""Elija idioma / Select language: 
                            1) Para español 
                            2) For english
                            """))




opciones["idioma"] = idioma

print(opciones["idioma"])




