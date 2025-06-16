from credicontrol1.modulo.pago import Pago
from credicontrol1.modulo.archivo import guardar_en_archivo, leer_desde_archivo
from datetime import datetime, timedelta
from credicontrol1.dao import prestamos_dao  

RUTA_PAGOS = "credicontrol1/data/pagos.txt"
pagos = leer_desde_archivo(RUTA_PAGOS, Pago)

def registrar_pago(pago):
    prestamo = prestamos_dao.buscar_prestamo(pago.id_prestamo)

    if prestamo:
      
        fecha_inicio = datetime.strptime(prestamo.fecha_prestamo, "%d-%m-%Y")
        if prestamo.frecuencia_pago.lower() == "mensual":
            dias_plazo = 30
        elif prestamo.frecuencia_pago.lower() == "quincenal":
            dias_plazo = 15
        elif prestamo.frecuencia_pago.lower() == "semanal":
            dias_plazo = 7
        else:
            dias_plazo = 30 

        fecha_limite = fecha_inicio + timedelta(days=dias_plazo)
        fecha_pago = datetime.strptime(pago.fecha, "%d-%m-%Y")

        if fecha_pago > fecha_limite:
            mora = prestamo.monto * 0.05  # 5% de mora
            print(f"⚠️ Pago atrasado. Se aplicará una mora de C${mora:.2f}.")
            pago.monto_pagado += mora

    pagos.append(pago)
    guardar_en_archivo(RUTA_PAGOS, pagos)
    prestamos_dao.actualizar_estado_prestamos() 

def listar_pagos():
    return pagos

def eliminar_pago(id_pago):
    global pagos
    pagos = [p for p in pagos if p.id_pago != id_pago]
    guardar_en_archivo(RUTA_PAGOS, pagos)

def pagos_por_prestamo(id_prestamo):
    return [p for p in pagos if p.id_prestamo == id_prestamo]

def total_pagado_por_prestamo(id_prestamo):
    return sum(p.monto_pagado for p in pagos if p.id_prestamo == id_prestamo)

