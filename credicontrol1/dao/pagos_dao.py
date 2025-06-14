from credicontrol1.modulo.pago import Pago
from credicontrol1.modulo.archivo import guardar_en_archivo, leer_desde_archivo


pagos = leer_desde_archivo("data/pagos.txt", Pago)

def registrar_pago(pago):
    pagos.append(pago)
    guardar_en_archivo("data/pagos.txt", pagos)
    
def listar_pagos():
    return pagos

def eliminar_pago(id_pago):
    global pagos
    pagos = [p for p in pagos if p.id_pago != id_pago]
    guardar_en_archivo("data/pagos.txt", pagos)

def pagos_por_prestamo(id_prestamo):
    return [p for p in pagos if p.id_prestamo == id_prestamo]