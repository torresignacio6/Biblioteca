import autor  # Módulo para manejar autores

# Clase Libro que hereda de autor
class Libro(autor):
    # Constructor que inicializa el ISBN, título y hereda el ID del autor
    def __init__(self, isbn, titulo, id_autor):
        super().__init__(id_autor)  # Hereda los atributos del autor usando su ID
        self.isbn = isbn  # Código ISBN del libro
        self.titulo = titulo  # Título del libro
    
    # Método para validar el formato del ISBN
    def validar_isbn(self):
        # Verifica que el ISBN tenga entre 10 y 13 caracteres y sea numérico
        if 10 <= len(self.isbn) <= 13 and self.isbn.isdigit():
            return True  # El ISBN es válido
        else:
            return False  # El ISBN no es válido
