
from views import vista_consola

from models.problema1_modelo import GestionEstudiantes
from models.problema2_modelo import GestionRutas
from models.problema3_modelo import GestionClinica
from models.problema4_modelo import GestionHistorial

def manejar_gestion_estudiantes():
    """Controla el flujo de la gestión de estudiantes."""
    gestor = GestionEstudiantes()
    gestor.agregar_estudiante("24020024", "Jairo", "De La Hoz", 55.0, 1.60, "Femenino", 85.5)
    gestor.agregar_estudiante("25010032", "Carlos", "Perez", 70.2, 1.75, "Masculino", 78.0)
    gestor.agregar_estudiante("20020241", "Luis", "Vega", 68.5, 1.70, "Masculino", 92.1)

    while True:
        opcion = vista_consola.mostrar_menu_estudiantes()

        if opcion == 1: 
            datos = vista_consola.pedir_datos_estudiante()
            exito, mensaje = gestor.agregar_estudiante(**datos)
            vista_consola.mostrar_mensaje(mensaje)

        elif opcion == 2: 
            if not gestor.obtener_estudiantes():
                 vista_consola.mostrar_mensaje("No hay estudiantes para ordenar.")
                 continue
            criterio = vista_consola.pedir_criterio_ordenamiento(gestor.CAMPOS_ORDENABLES)
            exito, mensaje = gestor.ordenar_estudiantes_por(criterio)
            vista_consola.mostrar_mensaje(mensaje)
            if exito: 
                 lista_actual = gestor.obtener_estudiantes()
                 vista_consola.mostrar_lista_estudiantes(lista_actual)


        elif opcion == 3: 
            lista_actual = gestor.obtener_estudiantes()
            vista_consola.mostrar_lista_estudiantes(lista_actual)

        elif opcion == 0: 
            print("Volviendo al menu")
            break

def manejar_calculo_ruta():
    """Controla el flujo del cálculo de rutas."""
    gestor = GestionRutas()
    gestor.agregar_estacion("Metrocentro", 10)
    gestor.agregar_estacion("Rotonda Rubén Darío", 5)
    gestor.agregar_estacion("Multicentro Las Américas", 0) 

    while True:
        opcion = vista_consola.mostrar_menu_ruta()

        if opcion == 1: 
            datos = vista_consola.pedir_datos_estacion()
            exito, mensaje = gestor.agregar_estacion(**datos)
            vista_consola.mostrar_mensaje(mensaje)

        elif opcion == 2: 
            ruta_actual = gestor.obtener_ruta()
            origen, destino = vista_consola.pedir_estacion_origen_destino(ruta_actual)
            if origen and destino:
                 exito, resultado = gestor.calcular_tiempo_ruta(origen, destino)
                 if exito:
                     vista_consola.mostrar_tiempo_estimado(resultado, origen, destino)
                 else:
                     vista_consola.mostrar_mensaje(f"Error al calcular: {resultado}")

        elif opcion == 3: 
            ruta_actual = gestor.obtener_ruta()
            vista_consola.mostrar_ruta(ruta_actual)

        elif opcion == 0: 
            print("Volviendo al menú principal...")
            break

def manejar_gestion_clinica():
    """Controla el flujo de la gestión de la clínica."""
    gestor = GestionClinica()
    gestor.ingresar_paciente("Snoopy Peanuts", 30, "Fiebre alta", 3)
    gestor.ingresar_paciente("Leana Raquel", 65, "Dolor de pecho", 1)


    while True:
        opcion = vista_consola.mostrar_menu_clinica()

        if opcion == 1:
            datos = vista_consola.pedir_datos_paciente()
            exito, mensaje = gestor.ingresar_paciente(**datos)
            vista_consola.mostrar_mensaje(mensaje)

        elif opcion == 2:
            paciente_atendido = gestor.atender_siguiente_paciente()
            vista_consola.mostrar_paciente_atendido(paciente_atendido)

        elif opcion == 3:
             paciente_proximo = gestor.ver_proximo_paciente()
             vista_consola.mostrar_proximo_paciente(paciente_proximo)

        elif opcion == 4: 
            cola_actual = gestor.obtener_cola_pacientes()
            vista_consola.mostrar_cola_pacientes(cola_actual)

        elif opcion == 0: 
            print("Volviendo al menú principal...")
            break

def manejar_historial_editor():
    """Controla el flujo del historial del editor."""
    gestor = GestionHistorial()

    while True:
        estado_actual = gestor.obtener_estado_actual()
        puede_deshacer = gestor.puede_deshacer()
        puede_rehacer = gestor.puede_rehacer()

        vista_consola.mostrar_estado_editor(estado_actual, puede_deshacer, puede_rehacer)
        opcion = vista_consola.mostrar_menu_editor()

        if opcion == 1:
            accion = vista_consola.pedir_accion_editor()
            if accion: 
                 gestor.realizar_accion(accion)
                 vista_consola.mostrar_mensaje("Acción registrada.")
            else:
                 vista_consola.mostrar_mensaje("Acción cancelada.")


        elif opcion == 2:
            if puede_deshacer:
                estado_anterior = gestor.deshacer()
                vista_consola.mostrar_mensaje(f"Deshacer realizado. Estado ahora: {estado_anterior}")
            else:
                vista_consola.mostrar_mensaje("No se puede deshacer más.")

        elif opcion == 3: 
            if puede_rehacer:
                estado_siguiente = gestor.rehacer()
                vista_consola.mostrar_mensaje(f"Rehacer realizado. Estado ahora: {estado_siguiente}")
            else:
                vista_consola.mostrar_mensaje("No se puede rehacer más.")

        elif opcion == 4:
             historial = gestor.obtener_historial_completo()
             cursor_pos = gestor.obtener_posicion_cursor()
             vista_consola.mostrar_historial_completo(historial, cursor_pos)


        elif opcion == 5:
             vista_consola.mostrar_estado_editor(estado_actual, puede_deshacer, puede_rehacer)


        elif opcion == 0:   
            print("Volviendo al menú principal...")
            break


def iniciar_aplicacion():
    """Inicia la aplicación principal y maneja el menú."""
    while True:
        opcion = vista_consola.mostrar_menu_principal()

        if opcion == 1:
            manejar_gestion_estudiantes()
        elif opcion == 2:
            manejar_calculo_ruta() 
        elif opcion == 3:
            manejar_gestion_clinica() 
        elif opcion == 4:
            manejar_historial_editor() 
        elif opcion == 0:
            print("Saliendo")
            break