const recordButton = document.getElementById('recordButton');
const stopButton = document.getElementById('stopButton');
const transcription = document.getElementById('transcription');
const removeButton = document.getElementById('removeButton');
const addButton = document.getElementById('addButton');
const cleanButton = document.getElementById('cleanButton');
function hablar(texto) {
    const mensaje = new SpeechSynthesisUtterance(texto);
    mensaje.lang = 'es-ES'; 
    window.speechSynthesis.speak(mensaje);
}

actualizarColaVisual();
hablar("Sigue trabajando duro, doctor Chapatín")

cleanButton.addEventListener('click', () => {
    transcription.value = '';
});

recordButton.addEventListener('click', async () => {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.ondataavailable = (event) => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
            const formData = new FormData();
            formData.append('audio', audioBlob, 'recording.webm');

            try {
                const response = await fetch('/transcribe', {
                    method: 'POST',
                    body: formData
                });
                const result = await response.json();
                transcription.value = result.text || result.error || 'No se recibió texto';
                hablar("Paciente a agregar: " + (result.text) || 'No se recibió texto');

                console.log('Transcripción:', result.text); 
                await actualizarColaVisual();
            } catch (error) {
                transcription.value = 'Error al enviar audio: ' + error.message;
            }

            stream.getTracks().forEach(track => track.stop());
        };

        mediaRecorder.start();
        recordButton.disabled = true;
        stopButton.disabled = false;
    } catch (error) {
        transcription.value = 'Error al iniciar grabación: ' + error.message;
    }
});

addButton.addEventListener('click', async () => {
    const texto = transcription.value.trim();

    if (texto === '' || texto === 'No se entendió el audio.' || texto.startsWith('Error') || texto.startsWith('⚠️')) {
        console.warn('Texto inválido, no se agregará a la cola:', texto);
        transcription.value = '⚠️ No se puede agregar ese texto.';
        return;
    }

    try {
        const response = await fetch('/agregar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                texto: texto
            })
        });

        const data = await response.json();

        if (!response.ok) {
            const errorMsg = data.error || 'Error en la solicitud al servidor';
            throw new Error(errorMsg);
        }

        console.log('Respuesta del servidor:', data);
        await actualizarColaVisual();
    } catch (error) {
        console.error('Error al añadir elemento a la cola:', error);
        transcription.value = 'Error al añadir elemento: ' + error.message;
    }
});

stopButton.addEventListener('click', () => {
    mediaRecorder.stop();
    recordButton.disabled = false;
    stopButton.disabled = true;
    actualizarColaVisual();
});


async function actualizarColaVisual() {
    try {
        const response = await fetch('/cola?_=' + new Date().getTime());
        if (!response.ok) throw new Error('Error al obtener la cola');
        const datos = await response.json();
        console.log('Datos de la cola:', datos); 

        const lista = document.querySelector('.cola-lista');
        if (!lista) throw new Error('Elemento .cola-lista no encontrado en el DOM');
        lista.innerHTML = '';  

        if (datos.length === 0) {
            const li = document.createElement('li');
            li.classList.add('text-muted');
            li.textContent = 'No hay elementos en la cola.';
            lista.appendChild(li);
        } else {
            datos.forEach(item => {
                const li = document.createElement('li');
                
                li.textContent = `${item[0]} - ${item[1]}`;
                lista.appendChild(li);
            });
        }
    } catch (error) {
        console.error('Error al actualizar la cola:', error);
        transcription.value = 'Error al cargar la cola: ' + error.message;
    }
}

actualizarColaVisual();

