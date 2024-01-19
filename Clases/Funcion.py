from CRUD import CRUD
class Funcion:
    def __init__(self, Nfuncion=None, hora_inicio=None, pelicula=None, fecha_estreno=None, hora_fin=None, costo_boleto=None):
        self.Nfuncion = Nfuncion
        self.hora_inicio = hora_inicio
        self.pelicula = pelicula
        self.fecha_estreno = fecha_estreno
        self.hora_fin = hora_fin
        self.costo_boleto = costo_boleto

    def __str__(self):
        return f"Funcion: {self.Nfuncion} \nHora de Inicio: {self.hora_inicio} \nPelícula: {self.pelicula} \nFecha de Estreno: {self.fecha_estreno} \nHora de Fin: {self.hora_fin} \nCosto de Boleto: {self.costo_boleto}"


    def to_dictionary(self):
        return vars(self)
