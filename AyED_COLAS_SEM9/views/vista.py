def mostrar_menu():
    """Renderiza el menú principal de la aplicación."""
    return """
    <h1>Centro de Salud León</h1>
    <button onclick="startVoiceRecognition()">Iniciar Reconocimiento de Voz</button>
    <ul id="patient-list"></ul>
    <script src="{{ url_for('static', filename='js/voice.js') }}"></script>
    """

def actualizar_lista_pacientes(pacientes):
    """Devuelve la lista de pacientes para la plantilla."""
    return pacientes