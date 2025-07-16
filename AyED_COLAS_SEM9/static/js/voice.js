document.addEventListener('DOMContentLoaded', function() {
    const startButton = document.getElementById('start-button');
    const patientList = document.getElementById('patient-list');

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();

    recognition.onstart = function() {
        startButton.textContent = 'Escuchando...';
        startButton.classList.add('recording');
        startButton.disabled = true;
    };

    recognition.onend = function() {
        startButton.textContent = 'Iniciar Reconocimiento de Voz';
        startButton.classList.remove('recording');
        startButton.disabled = false;
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript.toLowerCase();
        processCommand(transcript);
    };

    recognition.onerror = function(event) {
        alert('Error en reconocimiento: ' + event.error);
        startButton.textContent = 'Iniciar Reconocimiento de Voz';
        startButton.classList.remove('recording');
        startButton.disabled = false;
    };

    startButton.addEventListener('click', function() {
        recognition.start();
    });

    function processCommand(command) {
        if (command.includes('agregar paciente')) {
            const nombre = command.replace('agregar paciente', '').trim();
            if (nombre) {
                fetch('/enqueue', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ nombre: nombre })
                }).then(() => actualizarLista());
            }
        } else if (command.includes('atender paciente') || command.includes('pasar paciente')) {
            fetch('/dequeue', { method: 'POST' })
                .then(() => actualizarLista());
        } else {
            alert('Comando no reconocido. Usa "agregar paciente [nombre]" o "atender paciente".');
        }
    }

    function actualizarLista() {
        fetch('/cola')
            .then(response => response.json())
            .then(data => {
                patientList.innerHTML = '';
                if (data.length === 0) {
                    const li = document.createElement('li');
                    li.textContent = 'No hay pacientes en la cola.';
                    patientList.appendChild(li);
                } else {
                    data.forEach(nombre => {
                        const li = document.createElement('li');
                        li.textContent = nombre;
                        patientList.appendChild(li);
                    });
                }
            });
    }

    actualizarLista();
});