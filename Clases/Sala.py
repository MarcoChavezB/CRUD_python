class Sala:
    def __init__(self, numero=None, num_asientos=None, hora_limpieza=None, max_personas=None):
        self.numero = numero
        self.num_asientos = num_asientos
        self.hora_limpieza = hora_limpieza
        self.max_personas = max_personas
        self.funciones = []

    def __str__(self):
        funciones_str = "\n".join([str(funcion) for funcion in self.funciones])
        return f"Sala: {self.numero} \nNúmero de Asientos: {self.num_asientos} \nHora de Limpieza: {self.hora_limpieza} \nMáximo de Personas: {self.max_personas} \nFunciones:\n{funciones_str}"

    def to_dictionary(self):
        sala_dict = vars(self)
        sala_dict["funciones"] = [funcion.to_dictionary() for funcion in self.funciones]
        return sala_dict