from CRUD import CRUD
from Sala import Sala
from Funcion import Funcion
import json
import os
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
        if  [] == self.informacion:
            return f"Cine: {self.nombre} \nUbicacion: {self.ubicacion} \nHora de apertura: {self.hora_apertura} \nHora de cierre: {self.hora_cierre} \nSalas: {self.salas}"
        else:
            return f"array: {len(self.informacion)}"
        
    def to_dictionary(self):
        cine_dict = vars(self)
        cine_dict["salas"] = [sala.to_dictionary() for sala in self.salas]
        return cine_dict

    def save_to_json(self, file_path="informacionJSON.json"):
        existing_data = self.read_json(file_path)
        if existing_data is None:
            existing_data = []
        existing_data.append(self.to_dictionary())
        with open(file_path, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)


            
            
    def read_json(self, file_path="informacionJSON.json"):
        try:
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
            return data
        except FileNotFoundError:
            print(f"El archivo {file_path} no existe. Creando uno nuevo.")
            return None
        except json.decoder.JSONDecodeError:
            print(f"Error al cargar el archivo JSON en {file_path}. El archivo puede estar vacío o tener un formato no válido.")
            return None




if __name__ == '__main__': 
    from Sala import Sala
    from Funcion import Funcion
    from Cine import Cine
    os.remove("informacionJSON.json")
    cine = Cine(nombre="Cinemex", ubicacion="Torreon", hora_apertura="08:00", hora_cierre="22:00")
    cine2 = Cine(nombre="Cinepolis", ubicacion="Torreon", hora_apertura="08:00", hora_cierre="22:00")
    cine3 = Cine(nombre="Cinepolis", ubicacion="Torreon", hora_apertura="08:00", hora_cierre="22:00")
    sala = Sala(numero="b1", num_asientos=150, hora_limpieza="08:00", max_personas=200)
    sala2 = Sala(numero="b1", num_asientos=150, hora_limpieza="08:00", max_personas=200)
    sala3 = Sala(numero="b1", num_asientos=150, hora_limpieza="08:00", max_personas=200)
    funcion = Funcion(Nfuncion=1, hora_inicio="08:10", pelicula="spiderman", fecha_estreno="08/01/2024", hora_fin="10:20", costo_boleto=70)
    funcion2 = Funcion(Nfuncion=2, hora_inicio="10:10", pelicula="Superman", fecha_estreno="10/01/2024", hora_fin="12:20", costo_boleto=90)
    funcion3 = Funcion(Nfuncion=3, hora_inicio="10:10", pelicula="Superman", fecha_estreno="10/01/2024", hora_fin="12:20", costo_boleto=90)

    sala.funciones.append(funcion)
    sala2.funciones.append(funcion2)
    sala3.funciones.append(funcion3)
    
    cine.salas.append(sala)    
    cine2.salas.append(sala2)
    cine3.salas.append(sala3)
    
    cine.save_to_json()
    cine2.save_to_json()
    cine3.save_to_json()