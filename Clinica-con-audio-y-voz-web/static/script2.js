function hablar(texto) {
    const mensaje = new SpeechSynthesisUtterance(texto);
    mensaje.lang = 'es-ES'; 
    window.speechSynthesis.speak(mensaje);
}

function cargarPaciente() {
    fetch('/cola')
        .then(res => res.json())
        .then(data => {
            const pacienteBox = document.getElementById('pacienteAEliminar');
            if (data.length > 0) {
                pacienteBox.textContent = `${data[0][1]} (ID: ${data[0][0]})`;
                hablar(`Paciente a atender: ${data[0][1]}`);
                document.getElementById('quitarBtn').disabled = false;
            } else {
                pacienteBox.textContent = "No hay pacientes en la cola.";
                hablar("No hay pacientes en la cola.");
                document.getElementById('quitarBtn').disabled = true;
            }
        });
}

document.getElementById('quitarBtn').addEventListener('click', function() {
    fetch('/quitar', { method: 'POST' })
        .then(res => res.json())
        .then(data => {
            const mensaje = document.getElementById('mensaje');
            if (data.resultado) {
                mensaje.innerHTML = `<div class="alert alert-success">Paciente eliminado: <strong>${data.resultado}</strong></div>`;
                hablar("Paciente atendido correctamente");
            } else if (data.error) {
                mensaje.innerHTML = `<div class="alert alert-warning">${data.error}</div>`;
                hablar(data.error);
            }
            cargarPaciente();
        });
});

cargarPaciente();
