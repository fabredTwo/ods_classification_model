from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from modelo import Modelo 

obj = Modelo()
app = Flask(__name__)
CORS(app)
@app.route('/prediccionController', methods=['POST'])
def prediccionController():
    data = request.get_json()
    if 'texto' not in data:
        return jsonify({'error': 'Falta el campo "texto" en la solicitud'}), 400
    text = data['texto']
    try:
        pred = obj.prediccion(text)
        return jsonify({"prediccion": pred})
    except  Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    #app.run(debug=True)#-- para pruebas locales.
    app.run(host="0.0.0.0", port=5000)