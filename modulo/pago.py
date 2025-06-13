class Pago:
    def __init__(self, id_pago, id_prestamo, monto_pagado, fecha):
        self.id_pago = id_pago
        self.id_prestamo = id_prestamo
        self.monto_pagado = float(monto_pagado)
        self.fecha = fecha