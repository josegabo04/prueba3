import numpy as np
import random as ran
def grabar(datos):
    bool = True
    tipo = input("Ingrese el tipo de vehículo que desea ingresar:\n")
#    while True:
    patente=input("ingrese la patente del automóvil:\n")
        #for indice in range(patente):
            
    marca = input("ingrese la marca del vehículo:\n")
    while bool==True:
        try:
            precio=int(input("Ingrese el precio del vehiculo:\n"))
            if precio<=5000000:
                print("El precio debe ser mayor a $5.000.000")
            else:
                bool=False
        except:
            print("Ingrese un precio válido")
    multas=input("Ingrese el monto de las multas y sus fechas correspondientes(Si no posee ingrese 0):\n")
    fecharegistro=input("Igrese la fecha de registro del vehículo:\n")
    dueno=input("Ingrese el nombre del dueño del vehículo:\n")
    fila=np.array([tipo, patente, marca, precio, multas, fecharegistro,dueno])
    datos = np.append(datos,[fila],axis=0)
    return datos

def buscar(datos, filas):
    patente = input("Ingrese la patente del vehículo que desea buscar:\n")
    if patente not in datos:
        print("La patente ingresada no se encuentra en nuestros registros")
    else:
        for i in range(filas):
            if patente == datos[i][1]:
                print(datos[i][:])
    return

def imprimir(datos, filas):
    patente = input("Ingrese la patente del vehículo:\n")
    if patente not in datos:
        print("La patente ingresada no se encuentra en nuestros registros")
        return
    else:
        for i in range(filas):
            if patente == datos[i][1]:
                dueno = datos[i][6]
                regmulta = datos[i][4]
        op=2
        contam = ran.randint(1500,3000)
        anotac = ran.randint(1500,3000)
        multas = ran.randint(1500,3000)
        while op!=4:
            print("Ingrese el certificado que desea imprimir")
            print("1.- Emisión de contaminantes \t$", contam)
            print("2.- Anotaciones vigentes \t$", anotac)
            print("3.- Multas \t$", multas)
            print("4.- Volver")
            try: 
                op = int(input())
                if op<1 or op>4:
                    print("Ingrese una opción dentro del rango correspondiente")
                elif op == 1:
                    print("\t\t CERTIFICADO DE EMISIÓN DE CONTAMINANTES")
                    print("Patente:\t",patente)
                    print("Dueño del vehículo:\t",dueno )
                elif op == 2:
                    print("\t\t CERTIFICADO DE ANOTACIONES VIGENTES")
                    print("Patente:\t",patente)
                    print("Dueño del vehículo:\t",dueno )
                elif op == 3:
                    print("\t\t CERTIFICADO DE MULTAS")
                    print("Patente:\t",patente)
                    print("Dueño del vehículo:\t",dueno )
                    print("Multas:\t", regmulta)
            except:
                print("Ingrese una opcion válida")
    return