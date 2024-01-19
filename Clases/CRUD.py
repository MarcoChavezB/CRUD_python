import json
class CRUD:
    def __init__(self):
        self.informacion = []
    
    def show(self):
        for i in self.informacion:
            print(i)
    
    def add(self, diccionario):
        for i in diccionario.values():
            self.informacion.append(i)
        return "Se agrego correctamente"                
            
    def delete(self, index):
        if index < len(self.informacion):
            self.informacion.pop(index)
            return "Se eliminó correctamente"
        return "El indice no existe"
    
    def modificar_funcion(self, diccionario, nombre):
        for funcion in self.informacion:
            if funcion.nombre == nombre:
                for key, value in diccionario.items():
                    setattr(funcion, key, value)
            return "Se modificó correctamente"
        return "La función no existe"
    
    def to_dictionary(self):
        if len(self.informacion) == 0:
            return []
        else:
            dict_list = [vars(elemento) for elemento in self.informacion]
            with open("informacionJSON.json", "w") as archivo:
                json.dump(dict_list, archivo, indent=3)
            return dict_list

        
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

