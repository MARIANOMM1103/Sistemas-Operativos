'''PALABRAS'''

def contar_palabras(archivo):
    with open(archivo, 'r')as file:
        contenido=file.read()
        palabras=contenido.split()
        num_palabras=len(palabras)
        return num_palabras

archivo='Palabras.txt'
total_palabras=contar_palabras(archivo)
print("TOTAL:", total_palabras)
