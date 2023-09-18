#Aplicación que verifica si un archivo existe


import os

def verificar_archivo(nombre_archivo):
    return os.path.exists(nombre_archivo)



if __name__ == "__main__":
    print(verificar_archivo("hola.txt"))
