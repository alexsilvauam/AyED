// static/script.js
const recordButton = document.getElementById('recordButton');
const transcriptionArea = document.getElementById('transcriptionArea');
const statusMessage = document.getElementById('statusMessage');

recordButton.addEventListener('click', async () => {
    // Deshabilitar el botón y mostrar mensaje de estado
    recordButton.disabled = true;
    statusMessage.textContent = 'Grabando y procesando... Por favor, habla.';
    transcriptionArea.textContent = ''; // Limpiar área de transcripción previa
    transcriptionArea.classList.remove('error'); // Limpiar clase de error si estaba

    try {
        // Realizar la solicitud POST al backend de Flask
        const response = await fetch('/transcribe', {
            method: 'POST',
        });

        // Verificar si la respuesta fue exitosa
        if (!response.ok) {
            const errorData = await response.json().catch(() => null); // Intenta obtener JSON del error
            const errorMessage = errorData?.error || `Error del servidor: ${response.status} ${response.statusText}`;
            throw new Error(errorMessage);
        }

        // Convertir la respuesta a JSON
        const data = await response.json();

        // Mostrar el texto transcrito o el error
        if (data.error) {
            transcriptionArea.textContent = `Error: ${data.error}`;
            transcriptionArea.classList.add('error');
            statusMessage.textContent = 'Hubo un error.';
        } else if (data.text || data.text === "") { // Permitir texto vacío si es reconocido como tal
            transcriptionArea.textContent = data.text;
            statusMessage.textContent = '¡Transcripción completada!';
            if (data.text === "") {
                statusMessage.textContent = 'Se escuchó silencio o no se pudo transcribir claramente.';
            }
        } else {
            transcriptionArea.textContent = 'No se recibió texto ni error válido del servidor.';
            statusMessage.textContent = 'Respuesta inesperada del servidor.';
            transcriptionArea.classList.add('error');
        }

    } catch (error) {
        console.error('Error en la solicitud de transcripción:', error);
        transcriptionArea.textContent = `Error: ${error.message}`;
        transcriptionArea.classList.add('error');
        statusMessage.textContent = 'Error de comunicación o procesamiento.';
    } finally {
        // Volver a habilitar el botón
        recordButton.disabled = false;
        // Limpiar mensaje de estado después de un tiempo si no es un error persistente
        if (!transcriptionArea.classList.contains('error') && statusMessage.textContent && !statusMessage.textContent.toLowerCase().includes('error')) {
           setTimeout(() => {
                if (!recordButton.disabled) { // Solo limpiar si no se está procesando otra vez
                    statusMessage.textContent = '';
                }
           }, 4000);
        }
    }
});