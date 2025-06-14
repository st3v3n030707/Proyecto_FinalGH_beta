from credicontrol1.modulo.cliente import Cliente
from credicontrol1.modulo.prestamo import Prestamo
from credicontrol1.modulo.pago import Pago

from credicontrol1.dao import clientes_dao, prestamos_dao, pagos_dao

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
            fecha_prestamo = input("Fecha del préstamo (dd-mm-aaaa): ")
            prestamo = Prestamo(id_prestamo, id_cliente, monto, interes, cuotas, frecuencia, fecha_prestamo)
            prestamos_dao.crear_prestamo(prestamo)

        elif opcion == "3":
            id_pago = input("ID Pago: ")
            id_prestamo = input("ID Préstamo: ")
            monto_pagado = input("Monto pagado: ")
            fecha = input("Fecha (dd-mm-aaaa): ")
            pago = Pago(id_pago, id_prestamo, monto_pagado, fecha)
            pagos_dao.registrar_pago(pago)
            print("Pago registrado.")

        elif opcion == "4":
            for c in clientes_dao.listar_clientes():
                print(f"{c.id_cliente} - {c.nombre}")

        elif opcion == "5":
            for p in prestamos_dao.listar_prestamos():
                print(f"{p.id_prestamo} - Cliente: {p.id_cliente} - Monto: {p.monto} - Estado: {p.estado}")

        elif opcion == "6":
            for p in pagos_dao.listar_pagos():
                print(f"{p.id_pago} - Préstamo: {p.id_prestamo} - Monto: {p.monto_pagado} - Fecha: {p.fecha}")

        elif opcion == "7":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    mostrar_menu()

 