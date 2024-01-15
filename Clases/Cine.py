class Cine:
    arreglo = []
    def __init__(self=None, nombre=None, ubicacion=None, hora_apertura=None, hora_cierre=None, sala=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre
        self.salas = sala

    def __str__(self):
        print('')
        return f'Nombre: {self.nombre}, Ubicacion: {self.ubicacion},  Hora de Apertura: {self.hora_apertura},  Hora de Cierre: {self.hora_cierre}, Salas: {self.salas}\n'
