from modulo.prestamo import Prestamo
from modulo.archivo import guardar_en_archivo, leer_desde_archivo

prestamos = leer_desde_archivo("data/prestamos.txt", Prestamo)

def crear_prestamo(prestamo):
    prestamos.append(prestamo)
    guardar_en_archivo("data/prestamos.txt", prestamos)

def listar_prestamos():
    return prestamos
def eliminar_prestamo(id_prestamo):
    global prestamos
    prestamos = [p for p in prestamos if p.id_prestamo != id_prestamo]
    guardar_en_archivo("data/prestamos.txt", prestamos)

def buscar_prestamo(id_prestamo):
    for p in prestamos:
        if p.id_prestamo == id_prestamo:
            return p
    return None
