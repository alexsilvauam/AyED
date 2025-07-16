from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import subprocess
import os
from controller.dao import ColaDAO


colas = ColaDAO()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', cola=colas.retornar())

@app.route('/cola', methods=['GET'])
def obtener_cola():
    return jsonify(colas.retornar())

@app.route('/agregar', methods=['POST'])
def agregar():
    if request.method == 'POST':
        texto = request.form.get('texto')
        if texto:
            if colas.agregar(texto):
                return jsonify({'message': 'Texto agregado a la cola', 'cola': colas.retornar()})
            else:
                return jsonify({'error': 'El cliente ya esta en la cola'}), 400
        else:
            return jsonify({'error': 'No se proporcionó texto'}), 400
    return jsonify({'error': 'Método no permitido'}), 405

@app.route('/quitar', methods=['POST', 'GET'])
def quitar():
    if request.method == 'POST':
        resultado = colas.quitar()
        if resultado:
            return jsonify({'message': 'Texto quitado de la cola', 'resultado': resultado, 'cola': colas.retornar()})
        else:
            return jsonify({'error': 'No hay elementos en la cola'}), 400
    return render_template('quitar.html', cola=colas.retornar())

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({'error': 'No se proporcionó ningún archivo de audio'}), 400

    audio_file = request.files['audio']
    input_path = 'temp_input_audio.webm'
    output_path = 'temp_audio.wav'
    audio_file.save(input_path)
    print(f"Archivo guardado en {input_path}")
    print("Tamaño del archivo:", os.path.getsize(input_path), "bytes")

    ffmpeg_path = r"C:\Program Files\ffmpeg-2025-05-19-git-c55d65ac0a-essentials_build\bin\ffmpeg.exe"

    try:
        subprocess.run([ffmpeg_path, '-y', '-i', input_path, output_path], check=True)
    except subprocess.CalledProcessError as e:
        os.remove(input_path)
        return jsonify({'error': f'Error al convertir el audio con ffmpeg: {e}'}), 400

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(output_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        os.remove(input_path)
        os.remove(output_path)
        return jsonify({'error': 'No se entendió el audio.'}), 400
    except sr.RequestError as e:
        os.remove(input_path)
        os.remove(output_path)
        return jsonify({'error': f'Error con el servicio de reconocimiento: {e}'}), 400
    except Exception as e:
        os.remove(input_path)
        os.remove(output_path)
        return jsonify({'error': f'Error al procesar el audio: {e}'}), 400

    os.remove(input_path)
    os.remove(output_path)

    return jsonify({'text': text})


if __name__ == '__main__':
    app.run(debug=True)
