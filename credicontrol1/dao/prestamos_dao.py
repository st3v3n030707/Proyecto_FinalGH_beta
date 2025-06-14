from credicontrol1.modulo.prestamo import Prestamo
from credicontrol1.modulo.archivo import guardar_en_archivo, leer_desde_archivo

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

from credicontrol1.dao.pagos_dao import total_pagado_por_prestamo

def actualizar_estado_prestamos():
    for prestamo in prestamos:
        total = prestamo.monto + (prestamo.monto * prestamo.tasa_interes / 100)
        pagado = total_pagado_por_prestamo(prestamo.id_prestamo)
        if pagado >= total:
            prestamo.estado = "Pagado"
    guardar_en_archivo("credicontrol1/data/prestamos.txt", prestamos)
