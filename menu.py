

class Menu(object):
    __switcher = dict
    def __init__(self):
        self.__switcher = {1: self.Registrar, 2: self.Totaltarea, 3: self.ayuda, 4:self.Sueldos, 5: self.sueldoempleado,
                            11: self.modificarbasico,  12: self.modificarviatico, 13: self.modificarHora}
    def opcion(self, op, empleados):
        self.__switcher.get(op, lambda a: print("Opcion Incorrecta"))(empleados)

    def Registrar(self, empledos):
        if not empledos.incrementarhoras(input("Ingrese DNI: "), int(input("Ingrese Horas a incrementar: "))):
            print("Horas Registradas")
        else:
            print("No se encontro el Empleado")
    def Totaltarea(self, empledos):
        aux=empledos.tareasapagar(input("Ingrese Tarea: "))
        if aux !=0:
            print("El monto a pagar es: {:.2f}".format(aux))
        else:
            print("No se encontraron montos a pagar para la tarea")
    def ayuda(self, empledos):
        aux = empledos.ayuda()
        if aux != "":
            print(aux)
        else:
            print("No ha empleados que califiquen para la ayuda")
    def Sueldos(self, empledos):
        print(empledos.Sueldos())
    def sueldoempleado(self, empleados):
        emp = empleados.gastosSueldoPorEmpleado(input("Ingrese DNI: "))
        if emp == None:
            print("No se encontró el empleado")
        else:
            print("Sueldo: {}".format(emp))
    def modificarbasico(self, empleados):
        if empleados.modificarBasicoEPlanta(input("Ingrese DNI: "), float(input("Ingrese Nuevo Básico: "))):
            print("Basico, actualizado correctamente")
        else:
            print("No se encontro el empleado o no es empleado de planta")
    def modificarviatico(self, empleados):
        if empleados.modificarViaticoEExterno(input("Ingrese DNI: "), float(input("Ingrese Nuevo Viatico: "))):
            print("Valor de Viatico actualizado Correctamente")
        else:
            print("No se encontro el empleado o no es un empleado Externo")
    def modificarHora(self, empleados):
        if empleados.modificarValorEPorHora(float(input("Ingrese El valor de la hora: "))): #El Valor de hora es comun a todos los empleados
            print("Valor de hora Actualizado")
        else:
            print("Error al actualizar el valor de la hora")