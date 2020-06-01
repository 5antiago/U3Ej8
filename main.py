from datetime import date
from datetime import datetime
import csv
from menu import Menu
from coleccion import coleccion
from Empleadocontratado import EmpleadoContratado
from EmpleadoPlanta import EmpleadoPlanta
from EmpleadoExterno import EmpleadoExterno
from ITesorero import ITesorero
from IGerente import IGerente
import zope.interface
from zope.interface.verify import verifyObject 

def Gerente(empleado):
    menu = Menu()
    op = int(input("1. Modificar Báscio \n 2. Modificar Viatico \n 3. Modificar Valor de Hora \n 0. Salir \n Ingrese Opcion: " ))
    while op > 0:
        menu.opcion(op+10, empleado)
        op = int(input("1. Modificar Báscio \n 2. Modificar Viatico \n 3. Modificar Valor de Hora \n 0. Salir \n Ingrese Opcion: " ))

def Tesorero(empleado):
    menu = Menu()
    empleado.modificarBasicoEPlanta(" ", " ") #aqui llamo a un método de Gerete
    print(" 1. Registrar Horas \n 2. Total de la tarea \n 3. Ayuda a empleados \n 4. Sueldos \n 5. Sueldo Empleado \n 0. Salir")
    op = int(input("\n Ingrese opcion: "))
    while op > 0:
        menu.opcion(op,empleado)
        print(" 1. Registrar Horas \n 2. Total de la tarea \n 3. Ayuda a empleados \n 4. Sueldos \n 5. Sueldo Empleado \n 0. Salir")
        op = int(input("\n Ingrese opcion: "))


if __name__ == "__main__":
    empleados = coleccion(int(input("Ingrese cantidad de empleados: ")))
    with open("planta.csv") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            empleados.agregarempleado(EmpleadoPlanta(row[1],row[0], row[2], row[3], int(row[4]), int(row[5])))
    with open("contratados.csv") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            empleados.agregarempleado(EmpleadoContratado(row[1],row[0], row[2], row[3], 
            datetime.strptime(row[4], "%d/%m/%Y"), datetime.strptime(row[5], "%d/%m/%Y"), int(row[6]) ))
    with open("externos.csv") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            empleados.agregarempleado(EmpleadoExterno(row[1],row[0], row[2], row[3], row[4], 
            datetime.strptime(row[5], "%d/%m/%Y"), datetime.strptime(row[6], "%d/%m/%Y"), float(row[7]), float(row[8]), float(row[9]) ))
    
    user = input("Ingrese Usuario: ")
    password = input("Ingrese Contraseña: ")

    if user == "uTesorero" and password == "ag@74ck":
        Tesorero(ITesorero(empleados))

    elif user== "uGerente" and password =="ufC77#!1":
        Gerente(IGerente(empleados))
    else:
        print("Credenciales incorrectas")