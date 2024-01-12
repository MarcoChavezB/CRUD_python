
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


if __name__ == '__main__': 
    from Sala import Sala
    from Cine import Cine
    from Funcion import Funcion
    
    instancia = CRUD()
    funcion = Funcion(hora_inicio = '2:00 PM', pelicula = 'PeliculaXYZ', fecha_estreno = '2024-01-11', hora_fin = '4:00 PM', costo_boleto = '10.00')
    sala = Sala(numero = 100, num_asientos = 10, hora_limpieza = '10:00', max_personas = '12:00', funcion = funcion)
    cine = Cine(nombre = 'Cinemex', ubicacion = 'Torreon, Coahuila', hora_apertura = '10:00', hora_cierre = '12:00', sala = sala)
    objeto = {"sala": cine, "funcion": funcion}
    instancia.add(objeto)
    print(instancia.show())

    print("----------------------------------")
    
    #instancia.delete(1)
    instancia.modificar_funcion({"ubicacion": "3:002819821 PM"}, "Cinemex")
    print(instancia.show())

# funcion - sala - cines 