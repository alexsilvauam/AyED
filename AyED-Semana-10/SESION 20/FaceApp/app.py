from flask import Flask, render_template, request, jsonify
import face_recognition
import cv2
import numpy as np
import os
import base64

app = Flask(__name__)

# Ruta para almacenar las caras conocidas
KNOWN_FACES_DIR = "known_faces"
if not os.path.exists(KNOWN_FACES_DIR):
    os.makedirs(KNOWN_FACES_DIR)

# Cargar caras conocidas
known_face_encodings = []
known_face_names = []

def load_known_faces():
    global known_face_encodings, known_face_names
    for filename in os.listdir(KNOWN_FACES_DIR):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            name = os.path.splitext(filename)[0]
            image_path = os.path.join(KNOWN_FACES_DIR, filename)
            image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(image)
            if face_encoding:
                known_face_encodings.append(face_encoding[0])
                known_face_names.append(name)

# Cargar caras conocidas al iniciar
load_known_faces()

# Ruta principal
@app.route("/")
def index():
    return render_template("index.html")

#ruta Home
@app.route("/home")
def home():
    return render_template("home.html")

# Ruta para registrar una nueva cara
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    image_data = data.get("image")

    if not name or not image_data:
        return jsonify({"error": "Nombre o imagen no proporcionados"}), 400

    # Decodificar la imagen base64
    image_bytes = base64.b64decode(image_data.split(",")[1])
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Guardar la imagen
    image_path = os.path.join(KNOWN_FACES_DIR, f"{name}.jpg")
    cv2.imwrite(image_path, image)

    # Cargar la nueva cara
    face_encoding = face_recognition.face_encodings(image)
    if face_encoding:
        known_face_encodings.append(face_encoding[0])
        known_face_names.append(name)
        return jsonify({"success": True, "message": f"Cara de {name} registrada exitosamente"})
    else:
        return jsonify({"error": "No se detectó ninguna cara en la imagen"}), 400

# Ruta para autenticar un usuario
@app.route("/authenticate", methods=["POST"])
def authenticate():
    data = request.json
    image_data = data.get("image")

    if not image_data:
        return jsonify({"error": "Imagen no proporcionada"}), 400

    # Decodificar la imagen base64
    image_bytes = base64.b64decode(image_data.split(",")[1])
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Convertir a RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detectar caras
    face_locations = face_recognition.face_locations(rgb_image)
    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    if not face_encodings:
        return jsonify({"error": "No se detectó ninguna cara en la imagen"}), 400

    # Comparar con caras conocidas
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            return jsonify({"success": True, "name": name})

    return jsonify({"error": "Usuario no reconocido"})



if __name__ == "__main__":
    app.run(debug=True)

   
   
   
  
