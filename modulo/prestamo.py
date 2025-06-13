class Prestamo:
    def __init__(self, id_prestamo, id_cliente, monto, tasa_interes, cuotas, frecuencia_pago, estado="Activo"):
        self.id_prestamo = id_prestamo
        self.id_cliente = id_cliente
        self.monto = float(monto)
        self.tasa_interes = float(tasa_interes)
        self.cuotas = int(cuotas)
        self.frecuencia_pago = frecuencia_pago
        self.estado = estado
