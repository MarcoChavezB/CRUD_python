from CRUD import CRUD
class Sala(CRUD):
    def __init__(self=None, numero=None, num_asientos=None, hora_limpieza=None, max_personas=None, funcion=None):
        self.numSala = numero
        self.num_asientos = num_asientos
        self.hora_limpieza = hora_limpieza
        self.max_personas = max_personas
        self.funciones = Funcion()

    def __str__(self):
        print('')
        return f'Nombre de sala: {self.numSala}, numero de asientos: {self.num_asientos}, Funcion: {self.funcion}, hora de limpieza: {self.hora_limpieza}, maximo de personas: {self.max_personas}'


if __name__ == '__main__':
    from Cine import Cine
    from Funcion import Funcion
    funcion1 = Funcion('15:00', 'Spiderman', '08/01/2024', '17:30', 100)
    sala1 = Sala('B1', 100, '17:35', '90', funcion1)
    cine = Cine('Cinepolis', 'Torreon, Coahuila', '10:00', '12:00', None)
    
    sala1.funciones.add(funcion1)

    objeto = {"sala": sala1, "funcion": cine}
    crud = CRUD()
    crud.add(objeto)
    print(crud.show())
    
    
    print("----------------------------------")
    
    crud.delete(1)
    print(crud.show())