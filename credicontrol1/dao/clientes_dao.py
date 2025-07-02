from credicontrol1.modulo.cliente import Cliente #Importa la clase cliente desde el modulo correspondiente.
from credicontrol1.modulo.archivo import guardar_en_archivo, leer_desde_archivo #Importa funciones para guardar y leer archivos de texto.
RUTA_CLIENTES = "credicontrol1/data/clientes.txt" #Define la ruta donde se guardaran los archivos de texto.

clientes = leer_desde_archivo(RUTA_CLIENTES, Cliente) #Carga los clientes desde el archivo clientes.txt al iniciar el programa.

def registrar_cliente(cliente): #funcion para registrar un nuevo cliente.
    clientes.append(cliente) #Agrega el nuevo cliente a la lista.
    guardar_en_archivo(RUTA_CLIENTES, clientes) #Guarda la lista actualizada en el archivo clientes.txt.

# Busca un cliente por su ID
def buscar_cliente(id_cliente): #Funcion para buscar un cliente por su ID.
    for cliente in clientes: #Recorre cada cliente de la lista de clientes.
        if cliente.id_cliente == id_cliente: #Compara el ID del cliente actual con el que se busca.
            return cliente #retorna al cliente si lo encuentra.
    return None #si no lo encuentra retorna.

# Elimina un cliente por su ID
def eliminar_cliente(id_cliente): #Funcion para eliminar un cliente por su ID.
    global clientes #Declara que se utilizara la variable global clientes.
    clientes = [c for c in clientes if c.id_cliente != id_cliente] #Crea una nueva lista sin el cliente que se desea eliminar.
    guardar_en_archivo(RUTA_CLIENTES, clientes) #Guarda la lista actualizada en el archivo clientes.txt.

# Devuelve la lista de todos los clientes
def listar_clientes(): #Funcion para devolver todos los clientes registrados.
    return clientes # Retorna la lista completa de clientes.
