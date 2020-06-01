from datetime import datetime
from Empleado import Empleado

class EmpleadoContratado(Empleado):
    valorhora = 0.0
    __inicio = datetime
    __final = datetime
    __horas = int

    @classmethod
    def getvalorhora(cls):
        return cls.valorhora
    @classmethod
    def cambiarvalorhora(cls, valor):
        cls.valorhora = valor

    def __init__(self, dni, nom, dire, tel, ini, fin, hrs):
        super().__init__(dni, nom, dire, tel)
        self.__inicio = ini
        self.__final = fin
        self.__horas = hrs
    def getfechainic(self):
        return self.__inicio
    def getfechafinal(self):
        return self.__final
    def gethoras(self):
        return self.__horas
    def registrarhoras(self, horas):
        self.__horas += horas
    def Sueldo(self):
        return self.__horas * self.getvalorhora()