class Prestamo:
    def __init__(self, id_prestamo, id_cliente, monto, tasa_interes, cuotas, frecuencia_pago, fecha_prestamo, estado="Activo"):
        self.id_prestamo = id_prestamo
        self.id_cliente = id_cliente
        self.monto = float(monto)
        self.tasa_interes = float(tasa_interes)
        self.cuotas = int(cuotas)
        self.frecuencia_pago = frecuencia_pago
        self.fecha_prestamo = fecha_prestamo  # Nueva línea
        self.estado = estado