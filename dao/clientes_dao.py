from modulo.cliente import Cliente
from modulo.archivo import guardar_en_archivo, leer_desde_archivo

clientes = leer_desde_archivo("data/clientes.txt", Cliente)

def registrar_cliente(cliente):
    clientes.append(cliente)
    guardar_en_archivo("data/clientes.txt", clientes)

def buscar_cliente(id_cliente):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            return cliente