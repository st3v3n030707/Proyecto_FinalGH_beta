from credicontrol1.modulo.cliente import Cliente
from credicontrol1.modulo.prestamo import Prestamo
from credicontrol1.modulo.pago import Pago

from credicontrol1.dao import clientes_dao, prestamos_dao, pagos_dao

def mostrar_menu():
    while True:
        print("1. Registrar Cliente")
        print("2. Crear Préstamo")
        print("3. Registrar Pago")
        print("4. Ver Clientes")
        print("5. Ver Préstamos")
        print("6. Ver Pagos")
        print("7. Eliminar Cliente")
        print("8. Eliminar Préstamo")
        print("9. Eliminar Pago")
        print("10. Ver Detalles de un Préstamo")
        print("11. Salir")


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
            for c in clientes_dao.listar_clientes():
                print(f"{c.id_cliente} - {c.nombre}")
            id_cliente = input("Ingrese el ID del cliente a eliminar: ")
            clientes_dao.eliminar_cliente(id_cliente)
            print("Cliente eliminado.")

        elif opcion == "8":
            for p in prestamos_dao.listar_prestamos():
                print(f"{p.id_prestamo} - Cliente: {p.id_cliente} - Monto: {p.monto}")
            id_prestamo = input("Ingrese el ID del préstamo a eliminar: ")
            prestamos_dao.eliminar_prestamo(id_prestamo)
            print("Préstamo eliminado.")

        elif opcion == "9":
            for p in pagos_dao.listar_pagos():
                print(f"{p.id_pago} - Préstamo: {p.id_prestamo} - Monto: {p.monto_pagado}")
            id_pago = input("Ingrese el ID del pago a eliminar: ")
            pagos_dao.eliminar_pago(id_pago)
            print("Pago eliminado.")

        elif opcion == "10":
            id_prestamo = input("Ingrese el ID del préstamo: ")
            prestamo = prestamos_dao.buscar_prestamo(id_prestamo)
            if prestamo:
                total = prestamo.monto + (prestamo.monto * prestamo.tasa_interes / 100)
                pagado = pagos_dao.total_pagado_por_prestamo(id_prestamo)
                print(f"Monto del préstamo: C${prestamo.monto:.2f}")
                print(f"Interés: {prestamo.tasa_interes}%")
                print(f"Total a pagar: C${total:.2f}")
                print(f"Total pagado: C${pagado:.2f}")
                print(f"Estado del préstamo: {prestamo.estado}")
            else:
                 print("⚠️ Préstamo no encontrado.")


        elif opcion == "11":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    mostrar_menu()

 