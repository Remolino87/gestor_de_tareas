# Gestor de tareas

# Listas para almacenar las tareas
tareas =  []

def mostrar_tareas():
    """Función para mostrar todas las tareas en la losta."""
    print("\nTareas:")
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

def agregar_tarea(tarea):
    """Función para agregar una nueva tarea a la lista."""
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def eliminar_tarea(numero_tarea):
    """función para eliminar una tarea de la lista según su número. """
    if 0 < numero_tarea <= len(tareas):
        tarea = tareas.pop(numero_tarea - 1)
        print(f"Tarea '{tarea}' eliminada.")
    else:
        print("Número de tarea inválido.")

def gestor_tareas():
    """Función pincipal del gestor de tareas."""
    while True:
        print("\nGestor de Tareas")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")

        eleccion = input("Ingrese su elección (1/2/3/4): ")

        if eleccion == "1":
            mostrar_tareas()
        elif eleccion == "2":
            tarea = input("Ingrese la nueva tarea: ")
            agregar_tarea(tarea)
        elif eleccion == "3":
            mostrar_tareas()
            if tareas: # Solo pedir eliminar si hay tareas
                try:
                    numero_tarea = int(input("Ingrese el número de la tarea a eliminar: "))
                    eliminar_tarea(numero_tarea)
                except ValueError:
                    print("Entrada inválida, por favor ingrese un mumero.")
        elif eleccion == "4":
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Entrada inválida, por favor ingrese una opción válida.")
            
if __name__ == "___main___":
    gestor_tareas()


  