from credicontrol1.modulo.cliente import Cliente
from credicontrol1.modulo.archivo import guardar_en_archivo, leer_desde_archivo

RUTA_CLIENTES = "credicontrol1/data/clientes.txt"
clientes = leer_desde_archivo(RUTA_CLIENTES, Cliente)

def registrar_cliente(cliente):
    clientes.append(cliente)
    guardar_en_archivo(RUTA_CLIENTES, clientes)

def buscar_cliente(id_cliente):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            return cliente
    return None

def eliminar_cliente(id_cliente):
    global clientes
    clientes = [c for c in clientes if c.id_cliente != id_cliente]
    guardar_en_archivo(RUTA_CLIENTES, clientes)

def listar_clientes():
    return clientes
