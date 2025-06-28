import pwinput

RUTA_USUARIOS = "credicontrol1/data/usuarios.txt"

def cargar_usuarios():
    try:
        with open(RUTA_USUARIOS, "r") as archivo:
            return dict(linea.strip().split(",") for linea in archivo if "," in linea)
    except FileNotFoundError:
        return {}

def login():
    usuarios = cargar_usuarios()
    intentos = 3

    while intentos > 0:
        usuario = input("Usuario: ").strip()
        contrasena = pwinput.pwinput(prompt="Contraseña: ", mask="*")

        if usuario in usuarios and usuarios[usuario] == contrasena:
            print("Acceso concedido.")
            return True
        else:
            intentos -= 1
            print(f"Usuario o contraseña incorrectos. Te quedan {intentos} intento(s).\n")

    print("Acceso denegado.")
    return False
