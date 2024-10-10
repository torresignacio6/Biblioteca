import libro  # Módulo para manejo de libros
import editorial  # Módulo para manejo de editoriales

# Clase DetalleLibro que hereda de libro y editorial
class DetalleLibro(libro, editorial):
    # Constructor que inicia los atributos de detalle de un libro y hereda los datos de libro y editorial
    def __init__(self, id_detalle_libro, isbn, fecha_edicion, id_editorial, numero_paginas, id_categoria_libro, cantidad_ejemplares, ejemplares_disponibles):
        libro.__init__(isbn)
        editorial.__init__(id_editorial)  # Hereda la inicialización de la editorial con el ID
        self.id_detalle_libro = id_detalle_libro  # Identificador del detalle del libro, fecha y numero de paginas, categoria, cantidad de ejemplares y ejemplares  para prestar
        self.fecha_edicion = fecha_edicion  
        self.numero_paginas = numero_paginas  
        self.id_categoria_libro = id_categoria_libro  
        self.cantidad_ejemplares = cantidad_ejemplares 
        self.ejemplares_disponibles = ejemplares_disponibles
    # Sirve para actualizar la disponibilidad de ejemplares
    def actualizar_disponibilidad(self, origen, cantidad):
        # Si los ejemplares totales son mayores que los disponibles más la cantidad a modificar, si el origen es "retirar", reduce los ejemplares disponibles.
        if self.cantidad_ejemplares > self.ejemplares_disponibles + cantidad:
            if origen == "retirar":
                if self.ejemplares_disponibles > 0:
                    self.ejemplares_disponibles -= cantidad
                else:
                    print("No hay ejemplares disponibles para realizar el préstamo.")
            # Si no es "retirar", agrega ejemplares a los disponibles
            else:
                self.ejemplares_disponibles += cantidad
        else:
            print("Nuestros registros indican que hay un error en la cantidad de ejemplares.")
