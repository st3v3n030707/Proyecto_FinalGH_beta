#Definimos la clase Pago que representa un pago hecho por un cliente hacia in prestamo.
class Pago:

    #Metodo contructor para crear un nuevo pago.
    def __init__(self, id_pago, id_prestamo, monto_pagado, fecha):

        #Guardamos el ID del pago.
        self.id_pago = id_pago

        #Guardamos el ID del prestamo al que se aplica este pago.
        self.id_prestamo = id_prestamo

        #Convertimos el monto pagado a tipo float y lo guardamos.
        self.monto_pagado = float(monto_pagado)

        #Guardamos la fecha en que se realizo el pago.
        self.fecha = fecha