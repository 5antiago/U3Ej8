from datetime import datetime
from Empleado import Empleado

class EmpleadoExterno(Empleado):
    __tarea = str
    __inicio = datetime
    __final = datetime
    __viatico = float
    __costoobra = float
    __segvida = float

    def __init__(self, nom, dni, dire, tel, tarea, ini, fin, viat, costo, seg):
        super().__init__(nom, dni, dire, tel)
        self.__inicio = ini
        self.__final = fin
        self.__viatico = viat
        self.__costoobra = costo
        self.__segvida = seg
        self.__tarea = tarea
    def SetViatico(self, viatico):
        if type(viatico) == float:
            self.__viatico = viatico
    def gettarea(self):
        return self.__tarea
    def getinicio(self):
        return self.__inicio
    def getfinal(self):
        return self.__final
    def getviatico(self):
        return self.__viatico
    def getcostoobra(self):
        return self.__costoobra
    def getseguro(self):
        return self.__segvida
    def Sueldo(self):
        return self.__costoobra - self.__viatico - self.__segvida
