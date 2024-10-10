# Clase Paises que representa información básica sobre un país
class Paises():
    # Constructor que inicializa los atributos de un país
    def __init__(self, codigo_pais, codigo_iso3_pais, nombre_pais, gentilicio_pais):
        self.codigo_pais = codigo_pais  # Código numérico o alfabético del país
        self.codigo_iso3_pais = codigo_iso3_pais  # Código ISO 3 del país 
        self.nombre_pais = nombre_pais  # Nombre del país
        self.gentilicio_pais = gentilicio_pais  # Gentilicio del país
