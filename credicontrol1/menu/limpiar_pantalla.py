import os # Importa el módulo os para ejecutar comandos del sistema operativo
import platform # Importa platform para detectar el sistema operativo actual
def limpiar_pantalla(): # Función para limpiar la pantalla de la terminal
    if platform.system() == 'Windows':  # Verifica si el sistema operativo es Windows
        os.system('cls')   # Si es Windows, ejecuta el comando 'cls' para limpiar la consola
    else:
        os.system('clear')   # Si es Linux o macOS, ejecuta el comando 'clear'