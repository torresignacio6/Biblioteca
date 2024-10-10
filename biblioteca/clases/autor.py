from datetime import datetime # usamos datetime para trabajar con fechas
import paises # Clase externa para trabajar con países


# Clase Autor que hereda de paises
class Autor(paises):   #Constructor que inicializa los atributos de la clase Autor
    def __init__(self, id_autor, nombre_autor, seudonimo_autor, codigo_pais, fecha_nac, fecha_def, biografia_autor, foto_autor):
        super().__init__(codigo_pais) # Hereda el código de país de la clase paises
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.seudonimo_autor = seudonimo_autor
        self.fecha_nac = fecha_nac
        self.fecha_def = fecha_def
        self.biografia_autor = biografia_autor
        self.foto_autor = foto_autor
    
    def manejo_fechas(fecha):
        fecha_dt = datetime.strptime(fecha, '%d/%m/%Y')      # Método para convertir una fecha al formato 'YYYY-MM-DD'
        fecha_str = fecha_dt.strftime('%Y-%m-%d')
        return fecha_str