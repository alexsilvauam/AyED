# Centro de Salud León Flask Application

## Overview
This project is a web application for managing a patient queue at Centro de Salud León. It utilizes Flask for the backend and incorporates voice recognition functionality to allow users to manage the queue using voice commands.

## Project Structure
```
centro-salud-leon-flask
├── app.py                  # Entry point of the Flask application
├── requirements.txt        # Project dependencies
├── controllers             # Contains the control logic
│   ├── __init__.py        # Package initializer
│   └── controlador.py      # Manages interactions between voice commands and the patient queue
├── models                  # Contains data models
│   ├── __init__.py        # Package initializer
│   └── modelo.py          # Defines the patient queue model
├── static                  # Static files (CSS, JS, images)
│   └── js
│       └── voice.js        # JavaScript for voice recognition
├── templates               # HTML templates
│   └── index.html          # Main interface for the application
├── views                   # Contains view logic
│   ├── __init__.py        # Package initializer
│   └── vista.py            # Functions for rendering the web interface
└── README.md               # Project documentation
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd centro-salud-leon-flask
   ```

2. **Install dependencies**:
   Create a virtual environment and activate it, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```
   python app.py
   ```

4. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage
- Use the voice recognition button to add or remove patients from the queue.
- The patient queue will be displayed on the main interface, updating in real-time as commands are processed.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.