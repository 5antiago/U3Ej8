class Empleado(object):
    __Dni = str
    __nom = str
    __dir = str
    __tel = str

    def __init__(self, dni, nom, direc, tel):
        self.__Dni = dni
        self.__nom = nom
        self.__dir = direc
        self.__tel = tel
    def getdni(self):
        return self.__Dni
    def getnom(self):
        return self.__nom
    def getdir(self):
        return self.__dir
    def gettel(self):
        return self.__tel