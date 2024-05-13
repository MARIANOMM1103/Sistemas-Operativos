import subprocess
'''Autores: Mariano Martinez Marron
Emanuel Trinidad Garcia'''

def mostrar_menu():
    print("\nMenu de Opciones:")
    print("1. Crear archivo 'holamundo.txt'")
    print("2. Crear carpeta 'Python'")
    print("3. Crear carpeta 'Mis programas'")
    print("4. Mover 'holamundo.txt' a 'Mis programas'")
    print("5. Crear archivo 'Comandos.py' en 'Python'")
    print("6. Salir")
    return int(input("Seleccione una opción: "))

def crear_archivo(nombre_archivo):
    
    subprocess.run(['echo', '', '>', nombre_archivo], shell=True)
    print(f"Archivo '{nombre_archivo}' creado usando echo.")

def crear_directorio(directorio):
    
    subprocess.run(['mkdir', directorio])
    print(f"Carpeta '{directorio}' creada.")

def mover_archivo(origen, destino):
   
    subprocess.run(['cp', origen, destino])
    subprocess.run(['rm', origen])
    print(f"'{origen}' copiado y eliminado, efectivamente movido a '{destino}'.")

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            crear_archivo("holamundo.txt")
        elif opcion == 2:
            crear_directorio("Python")
        elif opcion == 3:
            crear_directorio("Mis programas")
        elif opcion == 4:
            mover_archivo("holamundo.txt", "Mis programas/holamundo.txt")
        elif opcion == 5:
            crear_archivo("Python/Comandos.py")
        elif opcion == 6:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
