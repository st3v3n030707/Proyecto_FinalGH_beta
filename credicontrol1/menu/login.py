# Importa la librería pwinput para ocultar la contraseña mientras se escribe
import pwinput

# Importa la función limpiar_pantalla desde el módulo correspondiente     
from credicontrol1.menu.limpiar_pantalla import limpiar_pantalla

# Ruta del archivo que contiene los usuarios registrados
RUTA_USUARIOS = "credicontrol1/data/usuarios.txt"

# Importa la función limpiar_pantalla para limpiar la consola
limpiar_pantalla()

# Imprime el título del login
print("== LOGIN ==")

# Función que carga los usuarios desde el archivo de texto
def cargar_usuarios(): #Define la función para cargar los usuarios

    try: # Abre el archivo de usuarios en modo lectura
        with open(RUTA_USUARIOS, "r") as archivo:
            # Lee cada línea y las convierte en un diccionario: usuario -> contraseña
            return dict(linea.strip().split(",") for linea in archivo if "," in linea)
    except FileNotFoundError:
         # Si no existe el archivo, retorna un diccionario vacío
        return {}

# Función principal de login
def login():
    usuarios = cargar_usuarios() # Carga los usuarios disponibles
    intentos = 3  # Número máximo de intentos permitidos

    # Bucle para intentar iniciar sesión
    while intentos > 0:
        usuario = input("\nUsuario: ").strip() # Solicita el nombre de usuario
        # Solicita la contraseña ocultando los caracteres con *
        contrasena = pwinput.pwinput(prompt="Contraseña: ", mask="*")

        # Verifica si el usuario y la contraseña son correctos
        if usuario in usuarios and usuarios[usuario] == contrasena:
            limpiar_pantalla()
            return True # Si el login es exitoso, limpia la pantalla y retorna True
        
        # Si el usuario o la contraseña son incorrectos
        else:
            intentos -= 1 # Resta un intento

            # Imprime un mensaje de error con el número de intentos restantes
            print(f"\n----- Usuario o contraseña incorrectos. Te quedan {intentos} intento(s). -----\n")

    # Si falla después de 3 intentos
    print("== Acceso denegado. ==") # Imprime mensaje de acceso denegado
    input("\nPresione ENTER para salir...") # Espera a que el usuario presione ENTER
    limpiar_pantalla() # Limpia la pantalla antes de salir
    return False # Retorna False indicando que el login falló
