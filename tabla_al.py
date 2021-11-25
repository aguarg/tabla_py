# Generador de una tabla de números aleatorios en formato txt, pdf o csv para imprimir.

# IMPORTAR MÓDULOS:
# Módulo para aleatorizar:
import random   

# Para manejar la consola de windows y linux creando una funcion clear(): 
from os import system, name 


# Opciones y estados:
opciones = {
    "idioma": 1,
    "cantidad_numeros": 0,
    "inicio": 0,
    "fin": 0,
    "formato": 0

}


# Función para limpiar la pantalla:
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


borrar()

