class Cine:
    def __init__(self=None, nombre=None, ubicacion=None, hora_apertura=None, hora_cierre=None, sala=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre
        self.salas = sala.numSala

    def __str__(self):
        print('')
        return f'Nombre: {self.nombre}, Ubicacion: {self.ubicacion}, Hora de Apertura: {self.hora_apertura}, Hora de Cierre: {self.hora_cierre}, Salas: {self.salas}'

if __name__ == '__main__':
    from Funcion import Funcion
    from Sala import Sala
    funcion1 = Funcion('15:00', 'Spiderman', '08/01/2024', '17:30', 100)
    sala1 = Sala('B1', 100, '17:35', '90', funcion1)
    cine = Cine('Cinepolis', 'Torreon, Coahuila', '10:00', '12:00', sala1)

    print(funcion1)
    print(sala1)
    print(cine)