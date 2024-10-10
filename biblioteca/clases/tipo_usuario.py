# Clase Tipo_Usuario que representa un tipo de usuario en el sistema
class Tipo_Usuario():
    # Constructor que inicializa los atributos del tipo de usuario
    def __init__(self, id_tipo_usuario, tipo_usuario, descripcion_tipo_usuario):
        self.id_tipo_usuario = id_tipo_usuario  # ID, nombre y descripcion del usuario.
        self.tipo_usuario = tipo_usuario  
        self.descripcion_tipo_usuario = descripcion_tipo_usuario 
