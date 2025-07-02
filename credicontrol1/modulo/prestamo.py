#Definimos la clase prestamo que representa un prestamo para un cliente.
class Prestamo:
    #Metodo constructor que inicializa  todos los datos del prestamo.
    def __init__(self, id_prestamo, id_cliente, monto, tasa_interes, cuotas, frecuencia_pago, fecha_prestamo, estado="Activo"):
        
        #Guardamos el ID del prestamo
        self.id_prestamo = id_prestamo

        #Guardamos el ID del cliente al que pertenece el prestamo.
        self.id_cliente = id_cliente

        #Convertimos el monto a tipo float y lo guardamos.
        self.monto = float(monto)

        #Convertimos la tasa de interes a tipo float y lo guardamos.
        self.tasa_interes = float(tasa_interes)

        #Convertimos el numero de cuotas a entero y lo almacenamos.
        self.cuotas = int(cuotas)

        #guardamos la frecuencia de pago (eje: semanal, quincenal, mensual).
        self.frecuencia_pago = frecuencia_pago

        #Guardamos la fecha en que se ortogo el prestamo.
        self.fecha_prestamo = fecha_prestamo  

        #Guardamos el estado del prestamo. Por defecto es "Activo".
        self.estado = estado

