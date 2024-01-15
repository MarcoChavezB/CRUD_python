from CRUD import CRUD
class Funcion(CRUD):
    funciones = []
    def __init__(self=None, hora_inicio=None, pelicula=None, fecha_estreno=None, hora_fin=None, costo_boleto=None):
        self.hora_inicio = hora_inicio
        self.movie = pelicula
        self.fecha_estreno = fecha_estreno
        self.hora_fin = hora_fin
        self.costo_boleto = costo_boleto
        self.funciones.append(self)


    def __str__(self):
        print('')
        return f'Hora de inicio: {self.hora_inicio}, Pelicula: {self.movie}, Fecha estreno: {self.fecha_estreno}, Hora de terminado: {self.hora_fin}, Costo de boleto: {self.costo_boleto}'



if __name__ == '__main__':
    from Cine import Cine
    from Sala import Sala
    funcion1 = Funcion('15:00', 'Spiderman', '08/01/2024', '17:30', 100)
    sala1 = Sala('B1', 100, '17:35', '90', funcion1)
    cine = Cine('Cinepolis', 'Torreon, Coahuila', '10:00', '12:00', sala1)
    
    
    
    
        
    
    
    