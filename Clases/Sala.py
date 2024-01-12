class Sala:
    def __init__(self, numero, num_asientos, hora_limpieza, max_personas, funcion):
        self.numSala = numero
        self.num_asientos = num_asientos
        self.hora_limpieza = hora_limpieza
        self.max_personas = max_personas
        self.funcion = funcion.movie

    def __str__(self):
        print('')
        return f'Nombre de sala: {self.numSala}, numero de asientos: {self.num_asientos}, Funcion: {self.funcion}, hora de limpieza: {self.hora_limpieza}, maximo de personas: {self.max_personas}'























if __name__ == '__main__':
    from Cine import Cine
    from Funcion import Funcion
    funcion1 = Funcion('15:00', 'Spiderman', '08/01/2024', '17:30', 100)
    sala1 = Sala('B1', 100, '17:35', '90', funcion1)
    cine = Cine('Cinepolis', 'Torreon, Coahuila', '10:00', '12:00', sala1)

    print(funcion1)
    print(sala1)
    print(cine)