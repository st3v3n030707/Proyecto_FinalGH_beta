import os
from credicontrol1.modulo.cliente import Cliente
from credicontrol1.modulo.prestamo import Prestamo
from credicontrol1.modulo.pago import Pago
from credicontrol1.dao import clientes_dao, prestamos_dao, pagos_dao
from credicontrol1.menu.login import login
from credicontrol1.modulo.limpiar_pantalla import limpiar_pantalla

def mostrar_menu():
    while True:
        limpiar_pantalla()
        print("=====================================")
        print("  SISTEMA DE GESTIÓN DE CRÉDITOS  ")
        print("=====================================")
        print("\nOpciones disponibles:")
        print("---------------------")
        print("1.	Registrar Cliente")
        print("2.	Crear Préstamo")
        print("3.	Registrar Pago")
        print("4.	Ver Clientes")
        print("5.	Ver Préstamos")
        print("6.	Ver Pagos")
        print("7.	Eliminar Cliente")
        print("8.	Eliminar Préstamo")
        print("9.	Eliminar Pago")
        print("10.	Ver Detalles de un Préstamo")
        print("11.	Salir")
        print("---------------------")

        opcion = input("\nSeleccione una opción (1-11): ")
        limpiar_pantalla()

        if opcion == "1":
            print("=== Registrar Cliente ===")
            id_cliente = input("ID Cliente: ").strip()
            nombre = input("Nombre: ").strip()

            if not id_cliente or not nombre:
                print("Ingrese datos válidos. No se permiten campos vacíos.")
            else:
                cliente = Cliente(id_cliente, nombre)
                clientes_dao.registrar_cliente(cliente)
                print("Cliente registrado exitosamente.")

            input("\nPresione Enter para continuar...")
            limpiar_pantalla()
            continue

        elif opcion == "2":
            print("=== Crear Préstamo ===")
            id_prestamo = input("ID Préstamo: ")
            id_cliente = input("ID Cliente: ")
            monto = input("Monto: ")
            interes = input("Tasa interés (%): ")
            cuotas = input("Número de cuotas: ")

            if not (id_prestamo and id_cliente and monto and interes and cuotas):
                print("Ingrese datos válidos. No se permiten campos vacíos.")
                input("\nPresione Enter para continuar...")
                limpiar_pantalla()
                continue

            try:
                monto = float(monto)
                interes = float(interes)
                cuotas = int(cuotas)
            except ValueError:
                print("Error: Monto, interés y cuotas deben ser numéricos.")
                input("\nPresione Enter para continuar...")
                limpiar_pantalla()
                continue

            print("\nFrecuencia de pago:")
            print("1.	Semanal")
            print("2.	Quincenal")
            print("3.	Mensual")
            frecuencia_opcion = input("Seleccione (1/2/3): ")

            if frecuencia_opcion == "1":
                frecuencia = "semanal"
            elif frecuencia_opcion == "2":
                frecuencia = "quincenal"
            elif frecuencia_opcion == "3":
                frecuencia = "mensual"
            else:
                frecuencia = "mensual"

            fecha_prestamo = input("Fecha del préstamo (dd-mm-aaaa): ")
            if not fecha_prestamo:
                print("Debe ingresar una fecha válida.")
                input("\nPresione Enter para continuar...")
                limpiar_pantalla()
                continue

            prestamo = Prestamo(id_prestamo, id_cliente, monto, interes, cuotas, frecuencia, fecha_prestamo)
            prestamos_dao.crear_prestamo(prestamo)
            print("Préstamo creado exitosamente.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "3":
            print("=== Registrar Pago ===")
            id_pago = input("ID Pago: ").strip()
            id_prestamo = input("ID Préstamo: ").strip()
            monto_pagado = input("Monto pagado: ").strip()
            fecha = input("Fecha (dd-mm-aaaa): ").strip()

            if not (id_pago and id_prestamo and monto_pagado and fecha):
                print("Ingrese datos válidos. No se permiten campos vacíos.")
                input("\nPresione Enter para continuar...")
                limpiar_pantalla()
                continue

            try:
                monto_pagado = float(monto_pagado)
            except ValueError:
                print("Error: El monto pagado debe ser un número.")
                input("\nPresione Enter para continuar...")
                limpiar_pantalla()
                continue

            pago = Pago(id_pago, id_prestamo, monto_pagado, fecha)
            pagos_dao.registrar_pago(pago)

            print("Pago ingresado exitosamente.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "4":
            print("=== Lista de Clientes ===")
            clientes = clientes_dao.listar_clientes()
            if clientes:
                for c in clientes:
                    print(f"ID: {c.id_cliente} | Nombre: {c.nombre}")
            else:
                print("No hay clientes registrados.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "5":
            print("=== Lista de Préstamos ===")
            prestamos = prestamos_dao.listar_prestamos()
            if prestamos:
                for p in prestamos:
                    print(f"ID: {p.id_prestamo} | Cliente: {p.id_cliente} | Monto: C${p.monto:.2f} | Estado: {p.estado} | Fecha: {p.fecha_prestamo}")
            else:
                print("No hay préstamos registrados.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "6":
            print("=== Lista de Pagos ===")
            pagos = pagos_dao.listar_pagos()
            if pagos:
                for p in pagos:
                    print(f"ID: {p.id_pago} | Préstamo: {p.id_prestamo} | Monto: C${p.monto_pagado:.2f} | Fecha: {p.fecha}")
            else:
                print("No hay pagos registrados.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "7":
            print("=== Eliminar Cliente ===")
            clientes = clientes_dao.listar_clientes()
            if clientes:
                for c in clientes:
                    print(f"ID: {c.id_cliente} | Nombre: {c.nombre}")
                id_cliente = input("\nIngrese el ID del cliente a eliminar: ")
                clientes_dao.eliminar_cliente(id_cliente)
                print("Cliente eliminado exitosamente.")
            else:
                print("No hay clientes registrados.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "8":
            print("=== Eliminar Préstamo ===")
            prestamos = prestamos_dao.listar_prestamos()
            if prestamos:
                for p in prestamos:
                    print(f"ID: {p.id_prestamo} | Cliente: {p.id_cliente} | Monto: C${p.monto:.2f}")
                id_prestamo = input("\nIngrese el ID del préstamo a eliminar: ")
                prestamos_dao.eliminar_prestamo(id_prestamo)
                print("Préstamo eliminado exitosamente.")
            else:
                print("No hay préstamos registrados.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "9":
            print("=== Eliminar Pago ===")
            pagos = pagos_dao.listar_pagos()
            if pagos:
                for p in pagos:
                    print(f"ID: {p.id_pago} | Préstamo: {p.id_prestamo} | Monto: C${p.monto_pagado:.2f}")
                id_pago = input("\nIngrese el ID del pago a eliminar: ")
                pagos_dao.eliminar_pago(id_pago)
                print("Pago eliminado exitosamente.")
            else:
                print("No hay pagos registrados.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "10":
            print("=== Detalles de Préstamo ===")
            id_prestamo = input("Ingrese el ID del préstamo: ")
            prestamo = prestamos_dao.buscar_prestamo(id_prestamo)
            if prestamo:
                total = prestamo.monto + (prestamo.monto * prestamo.tasa_interes / 100)
                pagado = pagos_dao.total_pagado_por_prestamo(id_prestamo)
                restante = total - pagado
                print("\nDetalles del Préstamo")
                print("---------------------")
                print(f"ID del préstamo: {prestamo.id_prestamo}")
                print(f"ID del cliente: {prestamo.id_cliente}")
                print(f"Fecha del préstamo: {prestamo.fecha_prestamo}")
                print(f"Monto del préstamo: C${prestamo.monto:.2f}")
                print(f"Interés: {prestamo.tasa_interes}%")
                print(f"Total a pagar: C${total:.2f}")
                print(f"Total pagado: C${pagado:.2f}")
                print(f"Saldo pendiente: C${restante:.2f}")
                print(f"Estado del préstamo: {prestamo.estado}")
            else:
                print("Préstamo no encontrado.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == "11":
            print("Saliendo del sistema...")
            input("\nPresione Enter para cerrar...")
            limpiar_pantalla()
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 11.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

if __name__  == "_main_":
    if login():
        mostrar_menu()