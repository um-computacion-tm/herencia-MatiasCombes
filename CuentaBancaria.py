class CuentaBancaria:
    def __init__(self, titular, monto, numero):
        self.__titular__ = titular
        self.__monto__ = monto
        self.__numero__ = numero

    def dame_saldo(self):
        return self.__monto__
    
    def deposito(self, monto_deposito):
        self.__monto__ += monto_deposito 
        
    def retirar(self, monto_retirar):
        self.__monto__ = self.__monto__ - monto_retirar









        