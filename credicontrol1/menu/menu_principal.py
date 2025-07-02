import os # Importa el módulo os que permite ejecutar comandos del sistema.
from credicontrol1.modulo.cliente import Cliente # Importa la clase Cliente desde el módulo correspondiente para registrar nuevos clientes.
from credicontrol1.modulo.prestamo import Prestamo # Importa la clase Prestamo para crear objetos de préstamo y asociarlos a clientes existentes.
from credicontrol1.modulo.pago import Pago # Importa la clase Pago para registrar los pagos realizados por los clientes.
from credicontrol1.dao import clientes_dao, prestamos_dao, pagos_dao # Importa los módulos DAO que permiten registrar, eliminar, buscar y listar datos guardados en archivos.
from credicontrol1.menu.login import login # Importa la función login que se usa para controlar el acceso al sistema.
from credicontrol1.menu.limpiar_pantalla import limpiar_pantalla # Importa la función que limpia la pantalla de la consola.

# Esta función muestra el menú principal del sistema y gestiona todas las opciones.
def mostrar_menu():
    while True:
        limpiar_pantalla()  # Limpia la pantalla al iniciar cada iteración del menu.
        print("=====================================")
        print("  SISTEMA DE GESTIÓN DE CRÉDITOS  ") # Título del sistema.
        print("=====================================")
        print("\nOpciones disponibles:") # Imprime las opciones disponibles en el menu.
        print("---------------------")
        print("1.	Registrar Cliente") # Opción para registrar un nuevo cliente.
        print("2.	Crear Préstamo") # Opción para crear un nuevo prestamo.
        print("3.	Registrar Pago") # Opción para registrar un nuevo pago.
        print("4.	Ver Clientes") # Opción para ver la lista de clientes.
        print("5.	Ver Préstamos") # Opción para ver la lista de préstamos.
        print("6.	Ver Pagos") # Opción para ver la lista de pagos.
        print("7.	Eliminar Cliente") # Opción para eliminar un cliente.
        print("8.	Eliminar Préstamo") # Opción para eliminar un préstamo.
        print("9.	Eliminar Pago") # Opción para eliminar un pago.
        print("10.	Ver Detalles de un Préstamo") # Opción para ver los detalles de un prestamo.
        print("11.	Salir") # Opción para salir del sistema.
        print("---------------------")

        opcion = input("\nSeleccione una opción (1-11): ") # Solicita al usuario que ingrese una opción del menu.
        limpiar_pantalla() # Limpia la pantalla después de que el usuario ingresa una opción.

        # opcion 1: Registrar cliente
        if opcion == "1": # Opción para registrar un nuevo cliente
            print("=== Registrar Cliente ===") # Imprime el título de la sección de registro de clientes.
            id_cliente = input("ID Cliente: ").strip() # Solicita el ID del cliente y elimina espacios en blanco al inicio y al final.
            nombre = input("Nombre: ").strip() # Solicita el nombre del cliente y elimina espacios en blanco al inicio y al final.

            # Verifica que los campos no estén vacíos
            if not id_cliente or not nombre:
                print("Ingrese datos válidos. No se permiten campos vacíos.") # Imprime un mensaje de error si los campos están vacíos.

                
            else: # Si los campos no están vacíos, crea un nuevo cliente
                cliente = Cliente(id_cliente, nombre) # Crea un objeto Cliente con el ID y nombre proporcionados.
                clientes_dao.registrar_cliente(cliente) # Llama a la función registrar_cliente del módulo clientes_dao para guardar el cliente.
                print("Cliente registrado exitosamente.") # Imprime un mensaje de éxito al registrar el cliente.

            input("\nPresione Enter para continuar...") # Espera a que el usuario presione Enter para continuar.
            limpiar_pantalla() # Limpia la pantalla antes de continuar con el siguiente ciclo del menu.
            continue # Continúa al inicio del bucle para mostrar el menu nuevamente.
        
                             #opcion 2: crear prestamo
        elif opcion == "2":
            print("=== Crear Préstamo ===") # Imprime el título de la sección de creación de préstamos.
            id_prestamo = input("ID Préstamo: ") # Solicita el ID del préstamo.
            id_cliente = input("ID Cliente: ") # Solicita el ID del cliente asociado al préstamo.
            monto = input("Monto: ") # Solicita el monto del préstamo.
            interes = input("Tasa interés (%): ") # Solicita la tasa de interés del préstamo.
            cuotas = input("Número de cuotas: ") # Solicita el número de cuotas del préstamo.

            # Verifica que los campos no estén vacíos
            if not (id_prestamo and id_cliente and monto and interes and cuotas):
                print("Ingrese datos válidos. No se permiten campos vacíos.") # Imprime un mensaje de error si algún campo está vacío.
                input("\nPresione Enter para continuar...") # Espera a que el usuario presione Enter para continuar.
                limpiar_pantalla() # Limpia la pantalla antes de continuar.
                continue # Continúa al inicio del bucle para mostrar el menu nuevamente.
                

            try:# Intenta convertir los valores ingresados a los tipos correctos
                monto = float(monto) # Convierte el monto a un número de punto flotante.
                interes = float(interes) # Convierte la tasa de interés a un número de punto flotante.
                cuotas = int(cuotas) # Convierte el número de cuotas a un entero.

                # Verifica que los valores sean positivos y no infinitos
                if not all([ 
                    monto > 0 and monto != float('inf'), # Verifica que el monto sea positivo y no infinito
                    interes > 0 and interes != float('inf'), # Verifica que la tasa de interés sea positiva y no infinita
                    cuotas > 0 # Verifica que el número de cuotas sea positivo
                ]):
                    raise ValueError # Si alguna de las condiciones anteriores falla, lanza una excepción ValueError.

            except ValueError: # Si ocurre un error al convertir los valores, imprime un mensaje de error.
                print("\nError: Monto, interés y cuotas deben ser números positivos válidos (no letras, negativos ni 'inf').")
                input("\nPresione Enter para continuar...")
                limpiar_pantalla() # Limpia la pantalla antes de continuar.
                continue # Continúa al inicio del bucle para mostrar el menu nuevamente.

            print("\nFrecuencia de pago:") #frecuencia de pago
            print("1.	Semanal")# Opción para seleccionar pago semanal
            print("2.	Quincenal")# Opción para seleccionar pago quincenal
            print("3.	Mensual")# Opción para seleccionar pago mensual
            
            frecuencia_opcion = input("Seleccione (1/2/3): ")# Solicita al usuario que seleccione una opción de frecuencia de pago.

            if frecuencia_opcion == "1": # Si el usuario selecciona la opción 1, establece la frecuencia de pago como semanal.
                frecuencia = "semanal"
            elif frecuencia_opcion == "2": # Si el usuario selecciona la opción 2, establece la frecuencia de pago como quincenal.
                frecuencia = "quincenal"
            elif frecuencia_opcion == "3": # Si el usuario selecciona la opción 3, establece la frecuencia de pago como mensual.
                frecuencia = "mensual"
            else:
                frecuencia = "mensual" #valor por defecto

            fecha_prestamo = input("Fecha del préstamo (dd-mm-aaaa): ") # Solicita la fecha del préstamo en formato día-mes-año.
            if not fecha_prestamo: # Verifica que se haya ingresado una fecha.
                print("Debe ingresar una fecha válida.")
                input("\nPresione Enter para continuar...")
                limpiar_pantalla()# Limpia la pantalla antes de continuar.
                continue # Continúa al inicio del bucle para mostrar el menu nuevamente.

            # Crea un objeto Prestamo con los datos ingresados
            prestamo = Prestamo(id_prestamo, id_cliente, monto, interes, cuotas, frecuencia, fecha_prestamo)
            # Llama a la función crear_prestamo del módulo prestamos_dao para guardar el préstamo.
            prestamos_dao.crear_prestamo(prestamo)
            print("Préstamo creado exitosamente.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

                            #opcion 3 :registrar pago
        elif opcion == "3":
            print("=== Registrar Pago ===") # Imprime el título de la sección de registro de pagos.
            id_pago = input("ID Pago: ").strip() # Solicita el ID del pago y elimina espacios en blanco al inicio y al final.
            id_prestamo = input("ID Préstamo: ").strip() # Solicita el ID del préstamo asociado al pago y elimina espacios en blanco al inicio y al final.
            monto_pagado = input("Monto pagado: ").strip() # Solicita el monto pagado y elimina espacios en blanco al inicio y al final.
            fecha = input("Fecha (dd-mm-aaaa): ").strip() # Solicita la fecha del pago en formato día-mes-año.

            # Verifica que los campos no estén vacíos
            if not (id_pago and id_prestamo and monto_pagado and fecha):
                print("Ingrese datos válidos. No se permiten campos vacíos.")
                input("\nPresione Enter para continuar...")
                limpiar_pantalla()
                continue

            try:# Intenta convertir el monto pagado a un número de punto flotante
                monto_pagado = float(monto_pagado)# Convierte el monto pagado a un número de punto flotante.
            
            
            except ValueError: # Si ocurre un error al convertir el monto pagado, imprime un mensaje de error.
                print("Error: El monto pagado debe ser un número.")
                input("\nPresione Enter para continuar...")
                limpiar_pantalla()
                continue

            pago = Pago(id_pago, id_prestamo, monto_pagado, fecha) # Crea un objeto Pago con los datos ingresados.
            pagos_dao.registrar_pago(pago)# Llama a la función registrar_pago del módulo pagos_dao para guardar el pago.

            print("Pago ingresado exitosamente.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

                            #opcion 4 :ver clientes
        elif opcion == "4":
            print("=== Lista de Clientes ===")
            clientes = clientes_dao.listar_clientes()# Llama a la función listar_clientes del módulo clientes_dao para obtener la lista de clientes.
            if clientes:# Si hay clientes registrados, los imprime en la consola.
                for c in clientes:# Itera sobre la lista de clientes y muestra su ID y nombre.
                    print(f"ID: {c.id_cliente} | Nombre: {c.nombre}") # Muestra el ID y nombre del cliente.

            else: # Si no hay clientes registrados, imprime un mensaje indicando que no hay clientes.
                print("No hay clientes registrados.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

                    #opcion 5: ver prestamos.
        elif opcion == "5":
            print("=== Lista de Préstamos ===")
            prestamos = prestamos_dao.listar_prestamos()# Llama a la función listar_prestamos del módulo prestamos_dao para obtener la lista de préstamos.
            if prestamos:# Si hay préstamos registrados, los imprime en la consola.
                for p in prestamos:# Itera sobre la lista de préstamos y muestra su ID, cliente, monto, estado y fecha.

                    # Muestra el ID del préstamo, ID del cliente, monto, estado y fecha del préstamo.
                    print(f"ID: {p.id_prestamo} | Cliente: {p.id_cliente} | Monto: C${p.monto:.2f} | Estado: {p.estado} | Fecha: {p.fecha_prestamo}")

            else:# Si no hay préstamos registrados, imprime un mensaje indicando que no hay préstamos.
                print("No hay préstamos registrados.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

                    #opcion 6: ver pagos
        elif opcion == "6":
            print("=== Lista de Pagos ===")
            pagos = pagos_dao.listar_pagos() # Llama a la función listar_pagos del módulo pagos_dao para obtener la lista de pagos.
            if pagos:# Si hay pagos registrados, los imprime en la consola.
                for p in pagos:# Itera sobre la lista de pagos y muestra su ID, préstamo, monto y fecha.
                    print(f"ID: {p.id_pago} | Préstamo: {p.id_prestamo} | Monto: C${p.monto_pagado:.2f} | Fecha: {p.fecha}")

            else:# Si no hay pagos registrados, imprime un mensaje indicando que no hay pagos.
                print("No hay pagos registrados.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla() # Limpia la pantalla antes de continuar.

                        #opcion 7: eliminar cliente.
        elif opcion == "7":
            print("=== Eliminar Cliente ===")
            clientes = clientes_dao.listar_clientes() # Llama a la función listar_clientes del módulo clientes_dao para obtener la lista de clientes.
            if clientes:# Si hay clientes registrados, los imprime en la consola.
                for c in clientes:# Itera sobre la lista de clientes y muestra su ID y nombre.
                    print(f"ID: {c.id_cliente} | Nombre: {c.nombre}")

                id_cliente = input("\nIngrese el ID del cliente a eliminar: ")# Solicita al usuario que ingrese el ID del cliente a eliminar.
                clientes_dao.eliminar_cliente(id_cliente)# Elimina el cliente de la base de datos.
                print("Cliente eliminado exitosamente.")

            # Si no hay clientes registrados, imprime un mensaje indicando que no hay clientes.
            else:
                print("No hay clientes registrados.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()


                            #opcion 8:Eliminar prestamo.
        elif opcion == "8":
            print("=== Eliminar Préstamo ===")
            prestamos = prestamos_dao.listar_prestamos()# Llama a la función listar_prestamos del módulo prestamos_dao para obtener la lista de préstamos.
            if prestamos:# Si hay préstamos registrados, los imprime en la consola.

                for p in prestamos:# Itera sobre la lista de préstamos y muestra su ID, cliente, monto y estado.
                    print(f"ID: {p.id_prestamo} | Cliente: {p.id_cliente} | Monto: C${p.monto:.2f}") # Muestra el ID del préstamo, ID del cliente y monto del préstamo.

                id_prestamo = input("\nIngrese el ID del préstamo a eliminar: ")# Solicita al usuario que ingrese el ID del préstamo a eliminar.
                prestamos_dao.eliminar_prestamo(id_prestamo)# Elimina el préstamo de la base de datos.
                print("Préstamo eliminado exitosamente.")

            else:# Si no hay préstamos registrados, imprime un mensaje indicando que no hay préstamos.
                print("No hay préstamos registrados.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()# Limpia la pantalla antes de continuar.

                            #opcion 9: Eliminar pago
        elif opcion == "9":
            print("=== Eliminar Pago ===")
            pagos = pagos_dao.listar_pagos()# Llama a la función listar_pagos del módulo pagos_dao para obtener la lista de pagos.

            if pagos:# Si hay pagos registrados, los imprime en la consola.
                for p in pagos:# Itera sobre la lista de pagos y muestra su ID, préstamo y monto.
                    print(f"ID: {p.id_pago} | Préstamo: {p.id_prestamo} | Monto: C${p.monto_pagado:.2f}")

                id_pago = input("\nIngrese el ID del pago a eliminar: ")# Solicita al usuario que ingrese el ID del pago a eliminar.
                pagos_dao.eliminar_pago(id_pago)# Elimina el pago de la base de datos.
                print("Pago eliminado exitosamente.")

            else: # Si no hay pagos registrados, imprime un mensaje indicando que no hay pagos.
                print("No hay pagos registrados.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()#

                            #opcion 10: ver detalles del prestamo.
        elif opcion == "10":
            print("=== Detalles de Préstamo ===")
            id_prestamo = input("Ingrese el ID del préstamo: ") # Solicita al usuario que ingrese el ID del préstamo para ver sus detalles.

            # Busca el préstamo por su ID
            prestamo = prestamos_dao.buscar_prestamo(id_prestamo)# Llama a la función buscar_prestamo del módulo prestamos_dao para obtener el préstamo correspondiente al ID ingresado.
            # Si el préstamo existe, muestra sus detalles
            if prestamo:
                # Calcula el total a pagar, el monto pagado y el saldo restante
                total = prestamo.monto + (prestamo.monto * prestamo.tasa_interes / 100)

                # Llama a la función total_pagado_por_prestamo del módulo pagos_dao para obtener el monto total pagado por el préstamo.
                pagado = pagos_dao.total_pagado_por_prestamo(id_prestamo)
                # Calcula el saldo restante
                restante = total - pagado

                print("\nDetalles del Préstamo") # Imprime los detalles del préstamo.
                print("---------------------") # Imprime una línea divisoria.
                print(f"ID del préstamo: {prestamo.id_prestamo}") # Muestra el ID del préstamo.
                print(f"ID del cliente: {prestamo.id_cliente}") # Muestra el ID del cliente asociado al préstamo.
                print(f"Fecha del préstamo: {prestamo.fecha_prestamo}") # Muestra la fecha del préstamo.
                print(f"Monto del préstamo: C${prestamo.monto:.2f}") # Muestra el monto del préstamo formateado a dos decimales.
                print(f"Interés: {prestamo.tasa_interes}%") # Muestra la tasa de interés del préstamo.
                print(f"Total a pagar: C${total:.2f}") # Muestra el total a pagar formateado a dos decimales.
                print(f"Total pagado: C${pagado:.2f}") # Muestra el total pagado formateado a dos decimales.
                print(f"Saldo pendiente: C${restante:.2f}") # Muestra el saldo pendiente formateado a dos decimales.
                print(f"Estado del préstamo: {prestamo.estado}") # Muestra el estado del préstamo.

            else: # Si el préstamo no existe, imprime un mensaje indicando que no se encontró.
                print("Préstamo no encontrado.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

                            #opcion 11:Salir del sistema.
        elif opcion == "11": # Opción para salir del sistema
            print("Saliendo del sistema...")
            input("\nPresione Enter para cerrar...")
            limpiar_pantalla()
            break # Sale del bucle y termina el programa.

        else:  # Si el usuario escribe una opción no válida
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 11.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()



if __name__  == "_main_":  # Inicia el sistema solo si el login es exitoso
    if login(): # Si el login es exitoso, muestra el menu principal.
        mostrar_menu() 