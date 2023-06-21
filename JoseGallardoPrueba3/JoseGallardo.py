import numpy as np
import random as ran
import funciones as fn

op=3
datos = np.empty((1,7), dtype=object)
while op!=4:
    print("\t\tMenú")
    print("1.- Grabar")
    print("2.- Buscar")
    print("3.- Imprimir certificados")
    print("4.- Salir")
    try:
        op=int(input())
        if op<1 or op>4:
            print("Ingrese una opción dentro del rango correspondiente")
        elif op == 1:
            datos = fn.grabar(datos)
            print(datos)
        elif op == 2:
            filas, columnas = datos.shape
            fn.buscar(datos, filas)
        elif op == 3:
            filas, columnas = datos.shape
            print()
        elif op == 4:
            break
    except:
        print("Ingrese una opción NUMERICA válida")
    