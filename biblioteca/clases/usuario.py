import paises  # Módulo para manejar información de países
import tipo_usuario  # Módulo para manejar tipos de usuarios
import re  # Módulo para trabajar con expresiones regulares
from rut_chile import rut_chile  # Módulo para validar que el rut es chileno

# Clase Usuario que representa la información de un usuario en el sistema
class Usuario(paises, tipo_usuario):
    # Constructor que inicializa los atributos del usuario
    def __init__(self, id_usuario, nombre_usuario, correo_usuario, telefono_usuario, rut_usuario, codigo_pais, habilitado, id_tipo_usuario, fecha_creacion):
        paises.__init__(codigo_pais)  # Inicializa la información del país
        tipo_usuario.__init__(id_tipo_usuario)  # Inicializa el tipo de usuario
        self.id_usuario = id_usuario  # ID del usuario
        self.nombre_usuario = nombre_usuario  # Nombre, correo, telefono, rut, estado de habilitacion y fecha de creacion del usuario.
        self.correo_usuario = correo_usuario 
        self.telefono_usuario = telefono_usuario  
        self.rut_usuario = rut_usuario  
        self.habilitado = habilitado 
        self.fecha_creacion = fecha_creacion 
    
    # Método para validar el RUT del usuario
    def validar_rut(self):
        return rut_chile.is_valid_rut(self.rut_usuario)  # Devuelve True si el RUT es válido
    
    # Método para validar el formato del correo electrónico
    def validar_correo(self):
        # Expresión regular para validar correos electrónicos
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, self.correo_usuario):
            return True  # El correo es válido
        else:
            return False  # El correo no es válido
