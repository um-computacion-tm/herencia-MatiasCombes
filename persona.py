class Persona:
    def __init__(self, nombre="", apellido="", du=()):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__du__ = du
    
    def __str__ (self):
        return f'Mis datos son nombre = {self.__nombre__} apellido = {self.__apellido__} documento = {self.__du__}'

    