from CRUD import CRUD
class Funcion(CRUD):
    informacion = []

    def __init__(self, Nfuncion=None, hora_inicio=None, pelicula=None, fecha_estreno=None, hora_fin=None, costo_boleto=None):
        super().__init__()
        self.Nfuncion = Nfuncion
        self.hora_inicio = hora_inicio
        self.pelicula = pelicula
        self.fecha_estreno = fecha_estreno
        self.hora_fin = hora_fin
        self.costo_boleto = costo_boleto

    def __str__(self):
        if  [] == self.informacion:
            return f"Funcion: {self.Nfuncion} \nHora de inicio: {self.hora_inicio} \nPelicula: {self.pelicula} \nFecha de estreno: {self.fecha_estreno} \nHora de fin: {self.hora_fin} \nCosto del boleto: {self.costo_boleto}"
        else:
            return f"array: {len(self.informacion)}"

    def to_dictionary(self):
        return vars(self)
