# Importa la librería pwinput para ocultar la contraseña mientras se escribe
import pwinput
from credicontrol1.modulo.limpiar_pantalla import limpiar_pantalla

# Ruta del archivo que contiene los usuarios registrados
RUTA_USUARIOS = "credicontrol1/data/usuarios.txt"

limpiar_pantalla()

print("== LOGIN ==")
# Función que carga los usuarios desde el archivo de texto
def cargar_usuarios():
    try:
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
            return True # Login exitoso
        else:
            intentos -= 1
            print(f"\n----- Usuario o contraseña incorrectos. Te quedan {intentos} intento(s). -----\n")

    # Si falla después de 3 intentos
    print("== Acceso denegado. ==")
    input("\nPresione ENTER para salir...")
    limpiar_pantalla()
    return False
