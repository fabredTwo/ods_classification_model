import json
import traceback
from modelo import Modelo

obj = None

def handler(event, context):

    global obj

    # ===== CARGA DEL MODELO (solo una vez) =====
    if obj is None:
        print("Cargando modelo buenamente...")
        obj = Modelo()
        print("Modelo listo")

    try:

        body = event.get("body")

        if body is None:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No se recibió body"})
            }

        try:
            data = json.loads(body)
        except:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "JSON inválido"})
            }

        if "texto" not in data:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": 'Falta el campo "texto"'})
            }

        texto = data["texto"]

        # ===== PREDICCIÓN =====
        pred = obj.prediccion(texto)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "prediccion": int(pred)
            })
        }

    except Exception as e:

        print("ERROR DETECTADO")
        traceback.print_exc()

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }