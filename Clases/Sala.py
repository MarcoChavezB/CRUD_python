from CRUD import CRUD
class Sala(CRUD):
    informacion = []

    def __init__(self, numero=None, num_asientos=None, hora_limpieza=None, max_personas=None):
        self.numSala = numero
        self.num_asientos = num_asientos
        self.hora_limpieza = hora_limpieza
        self.max_personas = max_personas
        self.funciones = []

    def __str__(self):
        if  [] == self.informacion:
            return f"Numero de sala: {self.numSala} \nNumero de asientos: {self.num_asientos} \nHora de limpieza: {self.hora_limpieza} \nMaximo de personas: {self.max_personas} \nFunciones: {self.funciones}"
        else:
            return f"array: {len(self.informacion)}"

    def to_dictionary(self):
        sala_dict = vars(self)
        sala_dict["funciones"] = [funcion.to_dictionary() for funcion in self.funciones]
        return sala_dict