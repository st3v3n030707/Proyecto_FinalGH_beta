import os

def guardar_en_archivo(nombre_archivo, lista_datos):
    os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)  # Crea la carpeta si no existe

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for item in lista_datos:
            archivo.write("|".join(str(valor) for valor in item.__dict__.values()) + "\n")


def leer_desde_archivo(nombre_archivo, clase):
    lista = []
    if not os.path.exists(nombre_archivo):
        return lista
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip() == "":
                continue  # Ignorar líneas vacías
            valores = linea.strip().split("|")
            try:
                objeto = clase(*valores)
                lista.append(objeto)
            except TypeError:
                print(f"Error al cargar: {valores} — estructura inválida")
    return lista

