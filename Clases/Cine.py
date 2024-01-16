from CRUD import CRUD
from Sala import Sala
import json
class Cine(CRUD):
    informacion = []

    def __init__(self, nombre=None, ubicacion=None, hora_apertura=None, hora_cierre=None):
        super().__init__()
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre
        self.salas = []

    def __str__(self):
        return f"Cine: {self.nombre} \nUbicacion: {self.ubicacion} \nHora de apertura: {self.hora_apertura} \nHora de cierre: {self.hora_cierre} \nSalas: {self.salas}"

    def to_dictionary(self):
        cine_dict = vars(self)
        cine_dict["salas"] = [sala.to_dictionary() for sala in self.salas]
        return cine_dict

    def save_to_json(self, file_path="informacionJSON.json"):
        cine_dict = self.to_dictionary()
        with open(file_path, "w") as json_file:
            json.dump(cine_dict, json_file, indent=4)
        print(f"JSON creado y guardado en '{file_path}'")
