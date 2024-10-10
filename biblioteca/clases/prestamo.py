from datetime import datetime, timedelta  # Para trabajar con fechas y tiempo
from auxiliares import constantes  # Módulo para constantes
import detalle_libro  # Módulo para manejar detalles de libros
import usuario  # Módulo para manejar información de usuarios

# Clase Prestamo que gestiona la información sobre préstamos de libros
class Prestamo(detalle_libro, usuario):
    # Constructor que inicializa los atributos de un préstamo
    def __init__(self, id_prestamo, isbn, id_usuario, fecha_prestamo, fecha_devolucion, fecha_devuelto, cantidad_solicitada):
        detalle_libro.__init__(isbn)  # Hereda detalles del libro usando el ISBN
        usuario.__init__(id_usuario)  # Hereda información del usuario usando el ID
        self.id_prestamo = id_prestamo  # Identificador del préstamo
        self.fecha_prestamo = fecha_prestamo  # Fecha en que se hizo el préstamo
        self.fecha_devolucion = fecha_devolucion  # Fecha para la devolución
        self.fecha_devuelto = fecha_devuelto  # Fecha cuando se devolvio
        self.cantidad_solicitada = cantidad_solicitada  # Cantidad de libros solicitada
    
    # Método para sumar días laborales a una fecha
    def sumar_dias_laborales(fecha_prestamo, dias_prestamo):
        dias_agregados = 0  
        while dias_agregados < dias_prestamo:
            fecha_prestamo += timedelta(days=1)  # Suma un día a la fecha
            # Verifica si el día es laboral y no está en la lista de festivos
            if fecha_prestamo.weekday() < 5 and fecha_prestamo not in constantes.festivos:
                dias_agregados += 1  # Incrementa el contador de días laborales
        return fecha_prestamo 
    
    # Método para calcular las fechas de préstamo y devolución
    def calcular_fechas(self):
        if self.ejemplares_disponibles > 0:  # Verifica si hay ejemplares disponibles
            if self.ejemplares_disponibles > self.cantidad_solicitada:  # Verifica si hay suficientes ejemplares
                self.fecha_prestamo = datetime.now()  # Establece la fecha de préstamo a la fecha actual
                self.fecha_devolucion = Prestamo.sumar_dias_laborales(self.fecha_prestamo, 5)  # Calcula la fecha de devolución
