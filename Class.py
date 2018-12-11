class Auto:
    def __init__(self,marka,tipus,uzemanyag,szin,rendszam,engedely):
        self.__marka=marka
        self.__tipus=tipus
        self.__uzemanyag=uzemanyag
        self.__szin=szin
        self.__rendszam=rendszam
        self.__engedely=engedely

    def getMarka(self):
        return self.__marka

    def getTipus(self):
        return self.__tipus

    def getUzemanyag(self):
        return self.__uzemanyag

    def getSzin(self):
        return self.__szin

    def getRendszam(self):
        return self.__rendszam

    def getEngedely(self):
        return self.__engedely

    def setMarka(self,marka):
        self.__marka=marka

    def setTipus(self,tipus):
        self.__tipus=tipus

    def setUzemanyag(self,uzemanyag):
        self.__uzemanyag=uzemanyag

    def setSzin(self,szin):
        self.__szin=szin

    def setRendszam(self,rendszam):
        self.__rendszam=rendszam

    def setEngedely(self,engedely):
        self.__engedely=engedely

    def __str__(self):
        return 'Rendszám: {} Márka: {} Típus: {} '.format(self.__rendszam,self.__marka,self.__tipus)

    def __eq__(self, other):
        return self.getRendszam()==other.getRendszam()

    def __le__(self, other):
        return self.getRendszam() <= other.getRendszam()

    def __gt__(self, other):
        return self.getRendszam() > other.getRendszam()


class HianyzoAdat(Exception):
    def __init__(self,valami):
        self.__valami=valami

    def __str__(self):
        return 'A '+self.__valami+' nincs megadva!'


class RendszamHiba(Exception):
    pass

class RendszamFormatumHiba(Exception):
    pass