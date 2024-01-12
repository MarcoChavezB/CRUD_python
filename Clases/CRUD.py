from Cine import Cine
from Funcion import Funcion
from Sala import Sala

class CRUD:
    informacion = []
    
    def show(self):
        for i in self.informacion:
            print(i)
    
    @staticmethod
    def add(nombre=None, ubicacion=None, hora_apertura=None, hora_cierre=None, sala_numero=None,
            sala_num_asientos=None, sala_hora_limpieza=None, sala_max_personas=None,
            funcion_hora_inicio=None, funcion_pelicula=None, funcion_fecha_estreno=None,
            funcion_hora_fin=None, funcion_costo_boleto=None):
        funcion = Funcion(funcion_hora_inicio, funcion_pelicula, funcion_fecha_estreno, funcion_hora_fin, funcion_costo_boleto)
        sala = Sala(sala_numero, sala_num_asientos, sala_hora_limpieza, sala_max_personas, funcion)
        cine = Cine(nombre, ubicacion, hora_apertura, hora_cierre, sala)
        CRUD.informacion.append(cine)
        return "Se agrego correctamente"
    
    def delete(self, nombre):
        for i in self.informacion:
            if i.nombre == nombre:
                self.informacion.remove(i)
                return "Se elimino correctamente"
        return "No se encontro el cine"
    
    def modificar(numero_sala, hora_apertura):
        for i in self.informacion:
            if i.sala_numero == numero_sala and i.hora_apertura ==  hora_apertura:
                 
        
            
        
if __name__ == '__main__':
    CRUD.add(nombre='Cinepolis', ubicacion='Torreon, Coahuila', hora_apertura='10:00', hora_cierre='12:00', sala_numero='1', sala_num_asientos=100, sala_hora_limpieza='12:00 PM', sala_max_personas=150, funcion_hora_inicio='2:00 PM', funcion_pelicula='PeliculaXYZ', funcion_fecha_estreno='2024-01-11', funcion_hora_fin='4:00 PM', funcion_costo_boleto='10.00')
    print(CRUD.show(CRUD))
    
    
    
    
    
    # from Funcion import Funcion
    # from Sala import Sala
    # funcion1 = Funcion('15:00', 'Spiderman', '08/01/2024', '17:30', 100)
    # sala1 = Sala('B1', 100, '17:35', '90', funcion1)
    # cine = Cine('Cinepolis', 'Torreon, Coahuila', '10:00', '12:00', sala1)

    # print(funcion1)
    # print(sala1)
    # print(cine)
    

#    agregar ver modificar y eliminar