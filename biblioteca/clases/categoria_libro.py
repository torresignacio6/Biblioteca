import tipo_categoria  # Módulo para manejar tipos de categorías


# Clase Categoria_Libro que hereda de tipo_categoria
class Categoria_Libro(tipo_categoria):
    # Constructor que inicia la categoría del libro y hereda
    def __init__(self, id_categoria_libro, id_tipo_categoria, categoria_libro):
        super().__init__(id_tipo_categoria)    # Hereda ID del tipo de categoría
        self.id_categoria_libro = id_categoria_libro   # ID de la categoría del libro
        self.categoria_libro = categoria_libro    # Nombre de la categoría del libro