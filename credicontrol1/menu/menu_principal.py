from modulo.cliente import Cliente
from modulo.prestamo import Prestamo
from modulo.pago import Pago

from dao import clientes_dao, prestamos_dao, pagos_dao

def mostrar_menu():
    while True:
        print("\n--- CrediControl ---")
        print("1. Registrar Cliente")
        print("2. Crear Préstamo")
        print("3. Registrar Pago")
        print("4. Ver Clientes")
        print("5. Ver Préstamos")
        print("6. Ver Pagos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_cliente = input("ID Cliente: ")
            nombre = input("Nombre: ")
            cliente = Cliente(id_cliente, nombre)
            clientes_dao.registrar_cliente(cliente)
            print("Cliente registrado.")