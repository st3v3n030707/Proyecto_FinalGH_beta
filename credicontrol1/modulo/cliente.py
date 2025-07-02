# Definimos la clase Cliente que representara a cada cliente del sistema.
class Cliente:
    #Metodo constructor de la clase cliente. Se ejecuta cuando se crea un nuevo objeto Cliente.
    def __init__(self, id_cliente, nombre):  
        #Asignamos el ID del cliente al atributo id_cliente.
        self.id_cliente = id_cliente
        #Asignamos el nombre del cliente al atributo nombre.
        self.nombre = nombre