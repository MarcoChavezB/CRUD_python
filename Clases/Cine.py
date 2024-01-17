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
            
            
    def read_json(self, file_path="informacionJSON.json"):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            return data
        
    def convert_to_object(self, json):
        data = self.read_json()
        
    
    



if __name__ == '__main__': 
    from Sala import Sala
    from Funcion import Funcion
    from Cine import Cine
    
    cine = Cine(nombre="Cinemex", ubicacion="Torreon", hora_apertura="08:00", hora_cierre="22:00")
    sala = Sala(numero="b1", num_asientos=150, hora_limpieza="08:00", max_personas=200)
    funcion = Funcion(Nfuncion=1, hora_inicio="08:10", pelicula="spiderman", fecha_estreno="08/01/2024", hora_fin="10:20", costo_boleto=70)
    funcion2 = Funcion(Nfuncion=2, hora_inicio="10:10", pelicula="Superman", fecha_estreno="10/01/2024", hora_fin="12:20", costo_boleto=90)

    sala.funciones.append(funcion)
    sala.funciones.append(funcion2)
    cine.salas.append(sala)

    cine.save_to_json()
    print(cine.read_json())