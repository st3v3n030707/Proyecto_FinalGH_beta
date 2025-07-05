
from credicontrol1.modulo.pago import Pago # Importa la clase Pago que representa un pago individual.
from credicontrol1.modulo.archivo import guardar_en_archivo, leer_desde_archivo # Importaa funciones para guardar y leer desde archivos de texto.
from datetime import datetime, timedelta # Importa las clases para manejar fechas y tiempos.
from credicontrol1.dao import prestamos_dao # Importa funciones del modulo  prestamos_dao para vincular pagos. 

# Ruta al archivo de pagos
RUTA_PAGOS = "credicontrol1/data/pagos.txt"# Ruta del archivo donde se almacenan los pagos.

# Carga los pagos desde el archivo
pagos = leer_desde_archivo(RUTA_PAGOS, Pago) #carga los pagos previamente almacenados almacenados desde el archivo a la lista 'pagos'.

# Registra un nuevo pago, calcula mora si es necesario y actualiza estado del préstamo
def registrar_pago(pago): #Define una funcion para registar un nuevo pago.
    prestamo = prestamos_dao.buscar_prestamo(pago.id_prestamo) #Busca el prestamo asociado al pago por su ID.

    if prestamo:
        fecha_inicio = datetime.strptime(prestamo.fecha_prestamo, "%d-%m-%Y")

            # Determina días por cada frecuencia
        if prestamo.frecuencia_pago.lower() == "mensual":
            dias_plazo = 30
        elif prestamo.frecuencia_pago.lower() == "quincenal":
            dias_plazo = 15
        elif prestamo.frecuencia_pago.lower() == "semanal":
            dias_plazo = 7
        else:
            dias_plazo = 30  # Valor por defecto

            # Número de pagos anteriores ya registrados
        pagos_anteriores = pagos_por_prestamo(pago.id_prestamo)
        cantidad_pagos = len(pagos_anteriores)

            # Calcula la fecha límite esperada para el siguiente pago
        fecha_limite = fecha_inicio + timedelta(days=dias_plazo * (cantidad_pagos + 1))

            #  Convierte la fecha actual del pago
        fecha_pago = datetime.strptime(pago.fecha, "%d-%m-%Y")

            #  Aplica mora solo si el pago está atrasado
        if fecha_pago > fecha_limite:
            mora = prestamo.monto * 0.05  # 5% de mora
            print(f"⚠️ Pago atrasado. Se aplicará una mora de C${mora:.2f}.")
            pago.monto_pagado += mora


    # Guarda el pago y actualiza estado
    pagos.append(pago) #agrega el nuevo pago a la lista. 
    guardar_en_archivo(RUTA_PAGOS, pagos) # guardar la lista actualizada de pagos en el archivo de texto.
    prestamos_dao.actualizar_estado_prestamos() # llama la funcion para actualizar los estados de los prestamos.


def listar_pagos(): #Funcion para listar todos los pagos registrados.
    return pagos #Retorna la lista de pagos.


def eliminar_pago(id_pago): # Funcion para eliminar un pago segun su ID.
    global pagos #indica que se utilizara la lista global 'pagos'.
    pagos = [p for p in pagos if p.id_pago != id_pago] #Filtra la lista excluyendo el pago con en el ID dado.
    guardar_en_archivo(RUTA_PAGOS, pagos) #Guarda la lista actualizada en el archivo de texto.


def pagos_por_prestamo(id_prestamo): # Funcion que devuleve todos los pagos realizados para un prestamo especifico.
    return [p for p in pagos if p.id_prestamo == id_prestamo] #Retorna una lista de pagos filtrada por el ID del prestamo.

def total_pagado_por_prestamo(id_prestamo): # funcion que suma el total pagado por un prestamo.
    return sum(p.monto_pagado for p in pagos if p.id_prestamo == id_prestamo) # Retorna la suma de todos los montos pagados asociadosa al prestamo.

