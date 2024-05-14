from persona import Persona

class Alumno(Persona):
    def __init__(self, apellido ="", du=()):
        self.__apellido__= apellido
        self.__du__= du
        
        super().__init__( apellido, du)