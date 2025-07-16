from models.modelo import ColaPacientes
from views.vista_web import VistaWeb
import speech_recognition as sr
import threading
import time

class Controlador:
    def __init__(self):
        self._modelo = ColaPacientes()
        self._vista = VistaWeb()
        self.recognizer = sr.Recognizer()
        self.command_thread = None
        self.is_running = True

    def iniciar(self):
        """Inicia la aplicación con interfaz web."""
        self._vista.mostrar_mensaje("Bienvenido al sistema de atención por voz del Centro de Salud León.")
        
        # Iniciar el thread para procesar comandos
        self.command_thread = threading.Thread(target=self.process_commands)
        self.command_thread.start()
        
        # Iniciar la aplicación web
        self._vista.iniciar()

    def process_commands(self):
        """Procesa los comandos de la cola de comandos."""
        while self.is_running:
            try:
                # Intentar obtener un comando de la cola
                comando = self._vista.command_queue.get(timeout=1)
                self.procesar_comando(comando)
            except:
                # Si no hay comandos, continuar
                time.sleep(0.1)
                continue

    def procesar_comando(self, comando):
        """Procesa los comandos recibidos."""
        if not comando:
            return

        # Interpretar comandos de voz
        if any(k in comando.lower() for k in ["registrar", "nuevo", "agregar"]):
            self.registrar_paciente()
        elif any(k in comando.lower() for k in ["atender", "siguiente"]):
            self.atender_paciente()
        elif any(k in comando.lower() for k in ["consultar", "próximo", "ver siguiente", "peek"]):
            self.consultar_siguiente()
        elif any(k in comando.lower() for k in ["mostrar cola", "ver cola", "estado cola"]):
            self.mostrar_cola()
        elif any(k in comando.lower() for k in ["salir", "terminar", "adiós"]):
            self._vista.mostrar_mensaje("Saliendo del sistema. ¡Hasta pronto!")
            self.is_running = False
        else:
            self._vista.mostrar_mensaje(f"Comando '{comando}' no reconocido. Por favor, intente de nuevo con uno de los comandos disponibles.")

    def registrar_paciente(self):
        """Registra un nuevo paciente usando reconocimiento de voz."""
        self._vista.mostrar_mensaje("Por favor, diga el nombre completo del paciente...")
        try:
            with sr.Microphone() as source:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                nombre = self.recognizer.recognize_google(audio, language="es-ES")
                if nombre:
                    self._modelo.enqueue(nombre)
                    self._vista.mostrar_mensaje(f"Paciente '{nombre}' agregado correctamente a la cola.")
                    self.actualizar_vista_cola()
                else:
                    self._vista.mostrar_mensaje("No se pudo reconocer el nombre del paciente. Intente registrar de nuevo.")
        except Exception as e:
            self._vista.mostrar_mensaje(f"Error al registrar paciente: {str(e)}")

    def atender_paciente(self):
        """Atiende al siguiente paciente en la cola."""
        if self._modelo.is_empty():
            self._vista.mostrar_mensaje("La cola está vacía, no hay pacientes para atender.")
        else:
            paciente_atendido = self._modelo.dequeue()
            self._vista.mostrar_mensaje(f"Atendiendo al paciente: {paciente_atendido}")
            self.actualizar_vista_cola()

    def consultar_siguiente(self):
        """Muestra el siguiente paciente en la cola."""
        if self._modelo.is_empty():
            self._vista.mostrar_mensaje("La cola está vacía, no hay próximo paciente.")
        else:
            siguiente = self._modelo.peek()
            self._vista.mostrar_mensaje(f"Próximo paciente a atender: {siguiente}")

    def mostrar_cola(self):
        """Muestra la cola completa de pacientes."""
        cola_actual = self._modelo.obtener_cola_completa()
        if not cola_actual:
            self._vista.mostrar_mensaje("La cola está vacía.")
        else:
            self._vista.mostrar_mensaje("Cola actual de pacientes:")
            for i, paciente in enumerate(cola_actual, 1):
                self._vista.mostrar_mensaje(f"{i}. {paciente}")

    def actualizar_vista_cola(self):
        """Actualiza la vista de la cola en la interfaz web."""
        cola_actual = self._modelo.obtener_cola_completa()
        self._vista.actualizar_cola(cola_actual)