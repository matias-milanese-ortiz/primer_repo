biblioteca = {}
def agregar_libro():
    id = input("Ingrese ID del libro: ")
    if id in biblioteca:
        print("El ID ya existe.")
    else:
        nombre = input("Ingrese nombre del libro ")
        autor = input("Ingrese el nombre del autor ")
        año_str = input("Ingrese año de creación del libro ")

        if (id == "") or (nombre == "") or (autor == "") or (año_str == ""):
            print("ID, nombre, autor y año no pueden estar vacíos.")
        else:
            try:
                año = int(año_str)
                biblioteca[id] = {"libro": nombre, "autor": autor, "año": año, "estado": "disponible"}
                print("Libro agregado.")
            except ValueError:
                print("El año debe ser un número entero.")
def consultar_libro():
    id = input("Ingrese ID del libro: ")
    if id in biblioteca:
        libro = biblioteca[id]
        print(libro["libro"], "-", libro["autor"], "-", libro["año"], "-", libro["estado"])
    else:
        print("ID no encontrada.")
def eliminar_libro():
    id = input("Ingrese matrícula del estudiante a eliminar: ")
    if id in biblioteca:
        biblioteca.pop(id)
        print("Estudiante eliminado.")
    else:
        print("Estudiante no encontrado.")
def modificar_libro():
    try:
        id_modificar = input("ID del libro a modificar: ")
    except ValueError:
        print("ID inválido.")
        return

    if id_modificar in biblioteca:
        libro = biblioteca[id_modificar]
        nuevo_titulo = input("Nuevo título (dejar vacío para no cambiar): ")
        nuevo_autor = input("Nuevo autor (dejar vacío para no cambiar): ")
        try:
            nuevo_año = input("Nuevo año (dejar vacío para no cambiar): ")
            if nuevo_año != "":
                nuevo_año = int(nuevo_año)
                libro["año"] = nuevo_año
        except ValueError:
            print("El año debe ser un número.")
            return

        if nuevo_titulo != "":
            libro["titulo"] = nuevo_titulo
        if nuevo_autor != "":
            libro["autor"] = nuevo_autor

        print("Libro actualizado.")
    else:
        print("Libro no encontrado.")
while True:
    print("\n--- Menú de Gestión de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Consultar libro")
    print("3. Modificar libro")
    print("4. Eliminar libro")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Debes ingresar un número.")
        continue

    if opcion == 1:
        agregar_libro()
    elif opcion == 2:
        consultar_libro()
    elif opcion == 3:
        modificar_libro()
    elif opcion == 4:
        eliminar_libro()
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")