from credicontrol1.menu.menu_principal import mostrar_menu # Importa la función mostrar_menu del módulo menu_principal
from credicontrol1.menu.login import login  # Importa la función login del módulo login

if __name__ == "__main__": # Verifica si este archivo es el principal que se está ejecutando.
    if login(): # Si el login es exitoso, muestra el menu principal.
        mostrar_menu()
