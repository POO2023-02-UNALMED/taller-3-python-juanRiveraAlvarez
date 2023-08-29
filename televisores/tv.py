class TV:
    _numTV = 0
    def __init__(self,marca,estado):
        self._marca = marca
        self._estado = estado
        TV._numTV = TV._numTV + 1

        self._canal = 1
        self._precio = 500
        self._volumen = 1

    def getMarca(self):
        return self._marca

    def getCanal(self):
        return self._canal

    def getPrecio(self):
        return self._precio

    def getVolumen(self):
        return self._volumen

    def getControl(self):
        return self._control

    def setMarca(self,marca):
        self._marca = marca

    def setCanal(self,canal):
        if self._estado and canal >= 1 and canal <=120:
            self._canal = canal

    def setPrecio(self,precio):
        self._precio = precio

    def setVolumen(self,volumen):
        if self._estado and volumen >=1 and volumen <= 7:
            self._volumen = volumen

    def setControl(self,control):
        self._control = control

    @staticmethod
    def getNumTV():
        return TV._numTV

    @staticmethod
    def setNumTV(numTV):
        TV.numTV = numTV

    def turnOff(self):
        self._estado = False

    def turnOn(self):
        self._estado = True

    def getEstado(self):
        return self._estado

    def canalUp(self):
        if self._estado and self._canal < 120:
            self._canal = self._canal + 1

    def canalDown(self):
        if self._estado and self._canal> 1:
            self._canal = self._canal - 1

    def volumenUp(self):
        if self._estado and self._volumen < 7:
            self._volumen = self._volumen + 1

    def volumenDown(self):
        if self._estado and self._volumen > 1:
            self._volumen = self._volumen - 1



