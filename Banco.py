from CuentaBancaria import CuentaBancaria

class CajaAhorro (CuentaBancaria):
    pass

class CuentaCorriente (CuentaBancaria):
    def __init__(self, titular, monto, numero, limite):
        super().__init__(titular, monto, numero)
        self.__limite__ = limite
        

















        