def mostrar_menu_principal():
        """Muestra el menú principal y devuelve la opción elegida."""
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestionar Estudiantes (Problema 1)")
        print("2. Calcular Ruta (Problema 2)")
        print("3. Gestionar Clínica (Problema 3)")
        print("4. Historial Editor (Problema 4)")
        print("0. Salir")
        while True:
            opcion = input("Seleccione una opción: ")
            if opcion.isdigit() and 0 <= int(opcion) <= 4:
                return int(opcion)
            else:
                print("Opción no válida. Intente de nuevo.")

def mostrar_menu_estudiantes():
    """Muestra el menú de gestión de estudiantes y devuelve la opción."""
    print("\n--- Gestión de Estudiantes ---")
    print("1. Agregar Estudiante")
    print("2. Ordenar Estudiantes")
    print("3. Mostrar Estudiantes")
    print("0. Volver al Menú Principal")
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion.isdigit() and 0 <= int(opcion) <= 3:
            return int(opcion)
        else:
            print("Opción no válida. Intente de nuevo.")

def pedir_datos_estudiante():
    """Solicita los datos de un nuevo estudiante al usuario."""
    print("\n--- Nuevo Estudiante ---")
    carnet = input("Carnet: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    while True:
        try:
            peso = float(input("Peso (kg): "))
            if peso > 0: break
            else: print("El peso debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número para el peso.")
    while True:
        try:
            estatura = float(input("Estatura (m): "))
            if estatura > 0: break
            else: print("La estatura debe ser positiva.")
        except ValueError:
            print("Entrada inválida. Ingrese un número para la estatura.")
    sexo = input("Sexo: ")
    while True:
        try:
            promedio = float(input("Promedio: "))
            if promedio >= 0: break
            else: print("El promedio no puede ser negativo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número para el promedio.")

    
    return {
        'carnet': carnet,
        'nombres': nombres,
        'apellidos': apellidos,
        'peso': peso,
        'estatura': estatura,
        'sexo': sexo,
        'promedio': promedio
    }

def pedir_criterio_ordenamiento(campos_validos):
    """Solicita el criterio para ordenar la lista de estudiantes."""
    print("\n--- Ordenar Estudiantes ---")
    print(f"Ordenar por (campos disponibles: {', '.join(campos_validos)}):")
    while True:
        criterio = input("Ingrese el campo por el cual ordenar: ").lower().strip()
        if criterio in campos_validos:
            return criterio
        else:
            print(f"Campo inválido. Por favor elija uno de: {', '.join(campos_validos)}")

def mostrar_lista_estudiantes(lista_estudiantes):
    """Muestra la lista de estudiantes de forma formateada."""
    print("\n--- Lista de Estudiantes ---")
    if not lista_estudiantes:
        print("No hay estudiantes para mostrar.")
        return
    for i, estudiante in enumerate(lista_estudiantes):
        print(f"{i + 1}. {estudiante}")
    print("-" * 25) 
def mostrar_mensaje(mensaje):
    """Muestra un mensaje informativo al usuario."""
    print(f"\n* {mensaje} *")


def mostrar_menu_ruta():
    print("\n--- Calcular Ruta ---")
    print("1. Agregar Estación al final")
    print("2. Calcular Tiempo entre Estaciones")
    print("3. Mostrar Ruta Completa")
    print("0. Volver al Menú Principal")
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion.isdigit() and 0 <= int(opcion) <= 3:
            return int(opcion)
        else:
            print("Opción no válida. Intente de nuevo.")

def pedir_datos_estacion():
    print("\n--- Nueva Estación ---")
    nombre = input("Nombre de la estación: ")
    while True:
        try:
            tiempo = float(input("Tiempo hasta la SIGUIENTE estación (minutos, 0 si es la última): "))
            if tiempo >= 0:
                break
            else:
                print("El tiempo no puede ser negativo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número para el tiempo.")
    return {'nombre': nombre, 'tiempo_siguiente': tiempo}

def pedir_estacion_origen_destino(lista_estaciones):
    print("\n--- Calcular Tiempo ---")
    if not lista_estaciones:
        print("No hay estaciones en la ruta para calcular.")
        return None, None
    print("Estaciones disponibles:", ", ".join([e.nombre for e in lista_estaciones]))
    while True:
        origen = input("Nombre de la estación de ORIGEN: ")
        if any(e.nombre.lower() == origen.lower() for e in lista_estaciones):
            break
        else:
            print(f"Estación '{origen}' no encontrada. Intente de nuevo.")

    while True:
        destino = input("Nombre de la estación de DESTINO: ")
        if any(e.nombre.lower() == destino.lower() for e in lista_estaciones):
             break
        else:
             print(f"Estación '{destino}' no encontrada. Intente de nuevo.")

    return origen, destino

def mostrar_ruta(lista_estaciones):
    print("\n--- Ruta Actual ---")
    if not lista_estaciones:
        print("La ruta está vacía.")
        return
    print(" -> ".join(map(str, lista_estaciones)))
    print("-" * 25)

def mostrar_tiempo_estimado(tiempo, origen, destino):
    print(f"\n* Tiempo estimado desde '{origen}' hasta '{destino}': {tiempo:.2f} minutos *")

def mostrar_menu_clinica():
    print("\n--- Gestión Clínica ---")
    print("1. Ingresar Paciente (al final de la cola)")
    print("2. Atender Siguiente Paciente (del inicio de la cola)")
    print("3. Ver Próximo Paciente")
    print("4. Mostrar Cola Completa")
    print("0. Volver al Menú Principal")
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion.isdigit() and 0 <= int(opcion) <= 4:
            return int(opcion)
        else:
            print("Opción no válida. Intente de nuevo.")

def pedir_datos_paciente():
    print("\n--- Nuevo Paciente ---")
    nombre = input("Nombre completo: ")
    while True:
        try:
            edad = int(input("Edad: "))
            if edad >= 0 : break
            else: print("La edad no puede ser negativa.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero para la edad.")
    sintoma = input("Síntoma principal: ")
    while True:
        try:
            prioridad = int(input("Prioridad (1-5): "))
            if 1 <= prioridad <= 5: break
            else: print("La prioridad debe estar entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero para la prioridad.")
    return {'nombre_completo': nombre, 'edad': edad, 'sintoma': sintoma, 'prioridad': prioridad}

def mostrar_cola_pacientes(lista_pacientes):
    print("\n--- Cola de Pacientes (Orden de Atención) ---")
    if not lista_pacientes:
        print("No hay pacientes en la cola.")
        return
    for i, paciente in enumerate(lista_pacientes):
        print(f"{i + 1}. {paciente}")
    print("-" * 25)

def mostrar_paciente_atendido(paciente):
    if paciente:
        mostrar_mensaje(f"Paciente atendido: {paciente}")
    else:
        mostrar_mensaje("No había pacientes en la cola para atender.")

def mostrar_proximo_paciente(paciente):
     if paciente:
        mostrar_mensaje(f"Próximo paciente a atender: {paciente}")
     else:
        mostrar_mensaje("La cola está vacía.")


def mostrar_menu_editor():
    print("\n--- Historial Editor ---")
    print("1. Realizar Acción")
    print("2. Deshacer (Undo)")
    print("3. Rehacer (Redo)")
    print("4. Mostrar Historial Completo")
    print("5. Mostrar Estado Actual")
    print("0. Volver al Menú Principal")
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion.isdigit() and 0 <= int(opcion) <= 5:
            return int(opcion)
        else:
            print("Opción no válida. Intente de nuevo.")

def pedir_accion_editor():
    print("\n--- Nueva Acción ---")
    accion = input("Describe la acción realizada (ej: 'Escribir hola', 'Borrar palabra'): ")
    return accion

def mostrar_historial_completo(historial, cursor_pos):
    print("\n--- Historial Completo ---")
    if not historial:
        print("El historial está vacío.")
        return
    for i, accion in enumerate(historial):
        prefijo = " --> " if i == cursor_pos else "     " # Indica el cursor
        print(f"{prefijo}{i}. {accion}")
    print("-" * 25)

def mostrar_estado_editor(estado, puede_deshacer, puede_rehacer):
    print("\n--- Estado Actual ---")
    print(f"Estado: {estado}")
    print(f"Puede Deshacer: {'Sí' if puede_deshacer else 'No'}")
    print(f"Puede Rehacer: {'Sí' if puede_rehacer else 'No'}")
    print("-" * 25)