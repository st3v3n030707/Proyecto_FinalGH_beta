from modulo.pago import Pago
from modulo.archivo import guardar_en_archivo, leer_desde_archivo

pagos = leer_desde_archivo("data/pagos.txt", Pago)

def registrar_pago(pago):
    pagos.append(pago)
    guardar_en_archivo("data/pagos.txt", pagos)