from Empleado import Empleado

class EmpleadoPlanta(Empleado): 
    __SB = float
    __antig = int

    def __init__(self, dni, nom, dire, tel, sb, ant):
        super().__init__(dni, nom, dire, tel)
        self.__SB = sb
        self.__antig = ant
    def getBasico(self):
        return self.__SB
    def getantiguedad(self):
        return self.__antig
    def SetBasico(self, basico):
        if type(basico)== float:
            self.__SB = basico
    def Sueldo(self):
        return self.__SB*0.01*self.__antig + self.__SB
        
