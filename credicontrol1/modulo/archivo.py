# Importamos el modulo os para trabajar con archivos y directorios.
import os

#Funcion para guardar una lista de objetos en un archivo de texto.
def guardar_en_archivo(nombre_archivo, lista_datos):
    #creamos la carpeta si no existe.
    os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True) 

    #Abrimos en el archivo en modo escritura (sobrescribe) y con codificación UTF-8. 
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:

        #Recorremos cada objeto en la lista de datos.
        for item in lista_datos:
            #Convertimos los atributos del objetivo a string y los separamos con "|", luego los escribimos en una linea.
            archivo.write("|".join(str(valor) for valor in item.__dict__.values()) + "\n")

#Funcion para leer los datos desde un archivo y convertirlos en objetos.
def leer_desde_archivo(nombre_archivo, clase):

    #Creamos una lista vacia para guardar los objetos leidos.
    lista = []

    #si el archivo no existe , devolvemos la lista vacia.
    if not os.path.exists(nombre_archivo):
        return lista # devuelve lista.
    
    #Abrimos el archivo en modo lectura y con codificación UTF-8.
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        #Leemos cada linea del archivo.
        for linea in archivo:
            #ignoramos las lineas vacias.
            if linea.strip() == "":
                continue  

            #Dividimos los datos por el caracterter "|" para obtener los valores.
            valores = linea.strip().split("|")

            try:
                #Intentamos crear un objeto usando la clase y los valores leidos.
                objeto = clase(*valores)

                #Agregamos el objeto a cada lista.
                lista.append(objeto)
            except TypeError:
                #Si hay un error de estructura , mostraremos un mensaje indicando los valores con error.
                print(f"Error al cargar: {valores} — estructura inválida")

    #Retornamos la lista de objetos leidos.
    return lista

