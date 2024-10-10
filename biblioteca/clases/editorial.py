import re  # Módulo para trabajar con expresiones regulares

# Clase Editorial que maneja la información básica de una editorial
class Editorial():
    # Constructor que inicializa los atributos de la editorial
    def __init__(self, id_editorial, nombre_editorial, fecha_fundacion, codigo_pais, telefono_contacto, correo_contacto):
        self.id_editorial = id_editorial  # ID de la editorial, nombre , fecha fundacion, codigo pais, numero telefono, correo de contacto.
        self.nombre_editorial = nombre_editorial  
        self.fecha_fundacion = fecha_fundacion  
        self.codigo_pais = codigo_pais  
        self.telefono_contacto = telefono_contacto  
        self.correo_contacto = correo_contacto  
    
    # Método para validar el formato del correo electrónico
    def validar_correo(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        # Verifica si el correo_contacto coincide con el formato del regex
        if re.fullmatch(regex, self.correo_usuario):
            return True  # El correo es válido
        else:
            return False  # El correo no es válido
