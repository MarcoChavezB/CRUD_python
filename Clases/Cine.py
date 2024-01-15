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
        return f'Nombre: {self.nombre},\n Ubicacion: {self.ubicacion}, \n Hora de Apertura: {self.hora_apertura}, \n Hora de Cierre: {self.hora_cierre},\n Salas: {self.salas}'
