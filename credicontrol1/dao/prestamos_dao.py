from credicontrol1.modulo.prestamo import Prestamo # Importa la clase desde el modulo correspondiente.
from credicontrol1.modulo.archivo import guardar_en_archivo, leer_desde_archivo #Importa funciones para guardar y leer datos desde el archivo de texto.
from credicontrol1.dao.pagos_dao import total_pagado_por_prestamo # Importa la función para calcular el total pagado por un préstamo.

RUTA_PRESTAMOS = "credicontrol1/data/prestamos.txt" #Define la ruta del archivo de texto donde se guardaran los prestamos.

prestamos = leer_desde_archivo(RUTA_PRESTAMOS, Prestamo) #Lee los prestamos almacenados en el archivo y los carga en la lista prestamos.

# Agrega un nuevo préstamo y lo guarda en archivo
def crear_prestamo(prestamo): #Define una funcion para crear y registar un nuevo prestamo.
    prestamos.append(prestamo) #Agrega un nuevo prestamo a la lista de prestamos.
    guardar_en_archivo(RUTA_PRESTAMOS, prestamos) #guarda la lista actuliazada  de prestamos en el archivo de texto.


# Busca un préstamo por su ID
def buscar_prestamo(id_prestamo): #define una funcion que busca un prestamo por su ID.
    for p in prestamos: #Recorre la lista de prestamos.
        if p.id_prestamo == id_prestamo: #Compara si el ID coincide con el que se busca.
            return p # si lo encuentra lo devuelve.
    return None # Si no lo encuentra, retorna None.

# Elimina un préstamo por ID
def eliminar_prestamo(id_prestamo): #Define una funcion para eliminar un prestamo por su ID.
    global prestamos #Declara que se utilizara la variable global prestamos.
    prestamos = [p for p in prestamos if p.id_prestamo != id_prestamo] #Crea una nueva lista sin el prestamo que se desea eliminar.
    guardar_en_archivo(RUTA_PRESTAMOS, prestamos) #Guarda la lista actualizada en el archivo prestamos.txt.

# Retorna la lista de todos los préstamos
def listar_prestamos(): #Define una funcion que retorna todos los prestamos registrados
    return prestamos #retorna toda la lista de prestamos.

# Revisa y actualiza el estado de los préstamos según si han sido pagados completamente

def actualizar_estado_prestamos(): #Define una funcion para actualizar el estado de los prestamos.
    for prestamo in prestamos: #recorre cada prestamo de la lista de prestamos.
        # Calcula el monto total a pagar (capital + interés)
        total = prestamo.monto + (prestamo.monto * prestamo.tasa_interes / 100)# Calcula el total a pagar sumando el monto del prestamo y el interes.
        pagado = total_pagado_por_prestamo(prestamo.id_prestamo)# Obtiene el total pagado por el prestamo utilizando la funcion total_pagado_por_prestamo.
        if pagado >= total: # Si el total pagado es mayor o igual al total a pagar, actualiza el estado del prestamo.
            prestamo.estado = "Pagado" # Cambia el estado del prestamo a "Pagado".
    guardar_en_archivo(RUTA_PRESTAMOS, prestamos) # Guarda la lista actualizada de prestamos en el archivo prestamos.txt.
