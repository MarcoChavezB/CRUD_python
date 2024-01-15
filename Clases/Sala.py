from CRUD import CRUD
from Funcion import Funcion

class Sala(CRUD):
    def __init__(self=None, numero=None, num_asientos=None, hora_limpieza=None, max_personas=None):
        self.numSala = numero
        self.num_asientos = num_asientos
        self.hora_limpieza = hora_limpieza
        self.max_personas = max_personas
        self.funciones = vars(Funcion())

    def __str__(self):    
        return f'Nombre de sala: {self.numSala}, numero de asientos: {self.num_asientos}, Funcion: {self.funciones}, hora de limpieza: {self.hora_limpieza}, maximo de personas: {self.max_personas}\n'

