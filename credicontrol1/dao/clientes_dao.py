# Importa la clase Cliente y funciones para manejar archivos
from credicontrol1.modulo.cliente import Cliente
from credicontrol1.modulo.archivo import guardar_en_archivo, leer_desde_archivo

# Ruta al archivo donde se guardan los clientes
RUTA_CLIENTES = "credicontrol1/data/clientes.txt"

# Carga los clientes desde el archivo
clientes = leer_desde_archivo(RUTA_CLIENTES, Cliente)


# Registra un nuevo cliente y guarda los datos en el archivo
def registrar_cliente(cliente):
    clientes.append(cliente)
    guardar_en_archivo(RUTA_CLIENTES, clientes)

# Busca un cliente por su ID
def buscar_cliente(id_cliente):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            return cliente
    return None

# Elimina un cliente por su ID
def eliminar_cliente(id_cliente):
    global clientes
    clientes = [c for c in clientes if c.id_cliente != id_cliente]
    guardar_en_archivo(RUTA_CLIENTES, clientes)

# Devuelve la lista de todos los clientes
def listar_clientes():
    return clientes
