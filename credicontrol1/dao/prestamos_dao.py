# Importa clase Prestamo y funciones de archivo
from credicontrol1.modulo.prestamo import Prestamo
from credicontrol1.modulo.archivo import guardar_en_archivo, leer_desde_archivo
from credicontrol1.dao.pagos_dao import total_pagado_por_prestamo

# Ruta al archivo de préstamos
RUTA_PRESTAMOS = "credicontrol1/data/prestamos.txt"

# Carga los préstamos desde el archivo
prestamos = leer_desde_archivo(RUTA_PRESTAMOS, Prestamo)

# Agrega un nuevo préstamo y lo guarda en archivo
def crear_prestamo(prestamo):
    prestamos.append(prestamo)
    guardar_en_archivo(RUTA_PRESTAMOS, prestamos)


# Busca un préstamo por su ID
def buscar_prestamo(id_prestamo):
    for p in prestamos:
        if p.id_prestamo == id_prestamo:
            return p
    return None

# Elimina un préstamo por ID
def eliminar_prestamo(id_prestamo):
    global prestamos
    prestamos = [p for p in prestamos if p.id_prestamo != id_prestamo]
    guardar_en_archivo(RUTA_PRESTAMOS, prestamos)

# Retorna la lista de todos los préstamos
def listar_prestamos():
    return prestamos

# Revisa y actualiza el estado de los préstamos según si han sido pagados completamente
def actualizar_estado_prestamos():
    for prestamo in prestamos:
        # Calcula el monto total a pagar (capital + interés)
        total = prestamo.monto + (prestamo.monto * prestamo.tasa_interes / 100)
        pagado = total_pagado_por_prestamo(prestamo.id_prestamo)
        if pagado >= total:
            prestamo.estado = "Pagado"
    guardar_en_archivo(RUTA_PRESTAMOS, prestamos)
