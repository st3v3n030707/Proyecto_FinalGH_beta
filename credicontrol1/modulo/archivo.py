import os

def guardar_en_archivo(nombre_archivo, lista_datos):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for item in lista_datos:
            archivo.write("|".join(str(valor) for valor in item.__dict__.values()) + "\n")

def leer_desde_archivo(nombre_archivo, clase):
    lista = []
    if not os.path.exists(nombre_archivo):
        return lista
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            valores = linea.strip().split("|")
            objeto = clase(*valores)
            lista.append(objeto)
    return lista
