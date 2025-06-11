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
            
        elif opcion == "2":
            id_prestamo = input("ID Préstamo: ")
            id_cliente = input("ID Cliente: ")
            monto = input("Monto: ")
            interes = input("Tasa interés (%): ")
            cuotas = input("Número de cuotas: ")
            frecuencia = input("Frecuencia de pago: ")
            prestamo = Prestamo(id_prestamo, id_cliente, monto, interes, cuotas, frecuencia)
            prestamos_dao.crear_prestamo(prestamo)
            print("Préstamo creado.")

        elif opcion == "3":
            id_pago = input("ID Pago: ")
            id_prestamo = input("ID Préstamo: ")
            monto_pagado = input("Monto pagado: ")
            fecha = input("Fecha (dd-mm-aaaa): ")
            pago = Pago(id_pago, id_prestamo, monto_pagado, fecha)
            pagos_dao.registrar_pago(pago)
            print("Pago registrado.")
