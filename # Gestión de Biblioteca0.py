# Gestión de Biblioteca
# Crear diccionario vacío para almacenar los datos
biblioteca = {}

# Definir las funciones
def agregar_libro():
    libro_id = input('Ingrese el ID del libro (debe ser único): ')
    if libro_id in biblioteca:
        print('Ya existe un libro con ese ID.')
        return

    titulo = input('Ingrese el título del libro que desea agregar: ')
    autor = input('Ingrese el autor del libro: ')
    
    try:
        año = int(input('Ingrese el año de publicación del libro: '))
    except ValueError:
        print('Hubo un error en el ingreso del año.')
        return

    estado = input('Ingrese el estado del libro (si=disponible / no=prestado): ').strip().lower()
    if estado not in ['si', 'no']:
        print('Estado inválido. Solo se permite "si" o "no".')
        return

    biblioteca[libro_id] = {
        'Titulo': titulo,
        'Autor': autor,
        'Año': año,
        'Estado': estado
    }
    print(f'Libro agregado exitosamente con el ID: {libro_id}')


def consultar_libro():
    if not biblioteca:
        print('No hay libros registrados.')
        return
    for libro_id, datos in biblioteca.items():
        print(f'\nID: {libro_id}')
        for clave, valor in datos.items():
            print(f'{clave}: {valor}')


def modificar_libro():
    libro_id = input('Ingrese el ID del libro a modificar: ')
    if libro_id not in biblioteca:
        print('No se encontró el ID ingresado.')
        return

    libro = biblioteca[libro_id]
    n_titulo = input(f"Título [{libro['Titulo']}]: ").strip()
    n_autor = input(f"Autor [{libro['Autor']}]: ").strip()
    n_año = input(f"Año [{libro['Año']}]: ").strip()
    n_estado = input(f"Estado (si/no) [{libro['Estado']}]: ").strip().lower()

    if n_titulo:
        libro['Titulo'] = n_titulo
    if n_autor:
        libro['Autor'] = n_autor
    if n_año:
        try:
            libro['Año'] = int(n_año)
        except ValueError:
            print('El año ingresado es incorrecto.')
    if n_estado in ['si', 'no']:
        libro['Estado'] = n_estado
    elif n_estado:
        print('Estado incorrecto. No se actualizó el estado.')

    print('Libro modificado exitosamente.')


def eliminar_libro():
    libro_id = input('Ingrese el ID del libro a eliminar: ')
    if libro_id in biblioteca:
        del biblioteca[libro_id]
        print('Libro eliminado con éxito.')
    else:
        print('No se encontró el ID ingresado.')


def menu_principal():
    while True:
        print('\n----- Menú Principal -----')
        print('1. Agregar Libro')
        print('2. Consultar Libros')
        print('3. Modificar Libro')
        print('4. Eliminar Libro')
        print('5. Salir')
        opcion_menu = input('Seleccione una opción del menú: ').strip()
        
        if opcion_menu == '1':
            agregar_libro()
        elif opcion_menu == '2':
            consultar_libro()
        elif opcion_menu == '3':
            modificar_libro()
        elif opcion_menu == '4':
            eliminar_libro()
        elif opcion_menu == '5':
            print('Hasta pronto. Saliendo del programa.')
            break
        else:
            print('La opción ingresada no es válida.')

menu_principal()
