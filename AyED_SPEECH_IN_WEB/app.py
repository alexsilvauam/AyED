
# -*- coding: utf-8 -*-
__version__ = "0.1.0" 

import speech_recognition as sr
from flask import Flask, render_template, request, jsonify
import logging
import os
import time # Para generar nombres de archivo únicos

# Configurar el logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# --- Configuración para guardar archivos ---
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegurarse de que la carpeta 'uploads' exista
if not os.path.exists(UPLOAD_FOLDER):
    try:
        os.makedirs(UPLOAD_FOLDER)
        app.logger.info(f"Carpeta '{UPLOAD_FOLDER}' creada exitosamente.")
    except OSError as e:
        app.logger.error(f"Error al crear la carpeta '{UPLOAD_FOLDER}': {e}")
# --- Fin de configuración para guardar archivos ---

r = sr.Recognizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    app.logger.info("Solicitud POST recibida en /transcribe")
    text = ""
    error = None
    saved_audio_filename = None
    saved_text_filename = None
    audio_data = None # Inicializar audio_data

    with sr.Microphone() as source:
        app.logger.info("Ajustando para ruido ambiente...")
        try:
            r.adjust_for_ambient_noise(source, duration=1)
            app.logger.info("¡Di algo!")
            audio_data = r.listen(source) # Capturamos el objeto AudioData
            app.logger.info("Audio capturado.")

            # --- 1. Guardar el archivo de audio ---
            if audio_data:
                try:
                    timestamp = time.strftime("%Y%m%d-%H%M%S")
                    audio_filename = f"audio_{timestamp}.wav"
                    audio_filepath = os.path.join(app.config['UPLOAD_FOLDER'], audio_filename)

                    with open(audio_filepath, "wb") as f:
                        f.write(audio_data.get_wav_data()) # Escribir datos WAV
                    saved_audio_filename = audio_filename
                    app.logger.info(f"Audio guardado en: {audio_filepath}")
                except Exception as e:
                    app.logger.error(f"Error al guardar el archivo de audio: {e}")
                    error = error + " (Error al guardar audio)" if error else "Error al guardar archivo de audio."
            else:
                app.logger.warning("No se capturó audio_data para guardar.")
            # --- Fin de guardar archivo de audio ---

            # --- 2. Transcribir el audio (si se capturó) ---
            if audio_data:
                app.logger.info("Procesando transcripción...")
                try:
                    text = r.recognize_google(audio_data, language='es-ES')
                    app.logger.info(f"Texto reconocido: {text}")

                    # --- 3. Guardar el texto transcrito ---
                    if text and saved_audio_filename: # Solo si hay texto y se guardó el audio
                        try:
                            # Usar el mismo timestamp para el archivo de texto
                            text_file_basename = os.path.splitext(saved_audio_filename)[0]
                            text_filename = f"{text_file_basename}.txt"
                            text_filepath = os.path.join(app.config['UPLOAD_FOLDER'], text_filename)
                            with open(text_filepath, "w", encoding="utf-8") as f:
                                f.write(text)
                            saved_text_filename = text_filename
                            app.logger.info(f"Texto transcrito guardado en: {text_filepath}")
                        except Exception as e:
                            app.logger.error(f"Error al guardar el archivo de texto: {e}")
                            # No sobrescribir error principal si ya existe uno
                            if not error:
                                error = "Error al guardar archivo de texto."
                    # --- Fin de guardar texto transcrito ---

                except sr.UnknownValueError:
                    error_msg = "Google Speech Recognition no pudo entender el audio."
                    app.logger.warning(error_msg)
                    error = error_msg
                except sr.RequestError as e:
                    error_msg = f"No se pudieron obtener resultados del servicio de Google Speech Recognition; {e}"
                    app.logger.error(error_msg)
                    error = error_msg
                except Exception as e:
                    error_msg = f"Ocurrió un error inesperado durante el reconocimiento: {e}"
                    app.logger.error(error_msg, exc_info=True)
                    error = error_msg
            elif not error: # Si no hubo error previo y no hay audio_data
                 error = "No se capturó audio para procesar."


        except sr.WaitTimeoutError:
            error = "No se detectó audio. Asegúrate de que el micrófono esté funcionando y que estés hablando."
            app.logger.warning(error)
        except Exception as e:
            error = f"Error al acceder al micrófono o al procesar el audio: {e}"
            app.logger.error(error, exc_info=True)

    return jsonify({
        'text': text,
        'error': error,
        'saved_audio_file': saved_audio_filename,
        'saved_text_file': saved_text_filename
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)