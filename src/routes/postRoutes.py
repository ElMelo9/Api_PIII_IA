import datetime
from database.crud_operations import Crud
from services.authLogin import AuthUser
from services.authToken import verificar_token
from flask import Blueprint, request, jsonify
from services.neuralPrediction import NeuralPredictor
import jwt
import os
import sys
from dotenv import load_dotenv
# Cargar variables de entorno desde el archivo .env
load_dotenv()
# Obtén la ruta del directorio actual
current_directory = os.path.dirname(os.path.realpath(__file__))
# Agrega el directorio raíz de tu proyecto al sys.path
project_directory = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.append(project_directory)

crud = Crud()
predictor = NeuralPredictor()
secret_key = os.getenv("SECRET_KEY")


post_routes = Blueprint('post_routes', __name__)

# Ruta para login
@post_routes.route('/login', methods=['POST'])
def login():
    auth = AuthUser()
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos de login no proporcionados"}), 400
    # credenciales
    email = data.get("email")
    password = data.get ("password")
    if not email or not password:
        return jsonify({"error": "datos incompletos para login!"}), 400
    # Llama a la función create_role para crear el rol en Supabase
    
    if auth.validate_credentials(email,password):
        info = {
    'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=1800)  # Vence en 30 minutos
    }
        # Si las credenciales son válidas, genera un token JWT
        token = jwt.encode(info,secret_key, algorithm='HS256')
        userData = crud.get_userByEmail(email)
        resultado = {'token': token, 'user_data': userData}
        return jsonify(resultado), 201
    else:
        return jsonify({'mensaje': 'Credenciales incorrectas'}), 401


# Ruta para crear un rol
@post_routes.route('/crear_rol', methods=['POST'])
@verificar_token
def crear_rol():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos del rol no proporcionados"}), 400
    # Nombre del rol a crear
    nombre_rol = data.get("nombre_rol")
    if not nombre_rol:
        return jsonify({"error": "Nombre de rol no proporcionado"}), 400
    # Llama a la función create_role para crear el rol en Supabase
    result = crud.create_role(data)
    if isinstance(result, Exception):
        return jsonify({"error": str(result)}), 500
    return jsonify({"message": f"Rol '{nombre_rol}' creado correctamente"}), 201


# Ruta para crear un tipo documento
@post_routes.route('/crear_document', methods=['POST'])
@verificar_token
def crear_document():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos del tipo documento no proporcionados"}), 400
    # Nombre del rol a crear
    identificacion = data.get("name_typedoc")
    if not identificacion:
        return jsonify({"error": "Nombre de tipo documento no proporcionado"}), 400
    # Llama a la función create_role para crear el rol en Supabase
    result = crud.create_document(data)
    if isinstance(result, Exception):
        return jsonify({"error": str(result)}), 500
    return jsonify({"message": f"tipo documento '{identificacion} creado correctamente"}), 201


# Ruta para crear un usuario
@post_routes.route('/crear_usuario', methods=['POST'])
@verificar_token
#@verificar_token
def crear_usuario():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos del usuario no proporcionados"}), 400
    # validar datos

    id_rol = data.get("id_rol")
    id_typedoc = data.get("id_typedoc")
    document_user= data.get("document_user")
    name_user= data.get("name_user")
    last_name_user= data.get("last_name_user")
    email_user= data.get("email_user")
    password_user= data.get("password_user")
    phone_user=data.get("phone_user")
    if not id_rol or not id_typedoc or not document_user or not name_user or not last_name_user or not email_user or not password_user or not phone_user:
        return jsonify({"error": "faltan datos para crear el usuario"}), 400
    # Llama a la función create_role para crear el rol en Supabase
    result = crud.create_user(data)
    if isinstance(result, Exception):
        return jsonify({"error": str(result)}), 500
    return jsonify({" message": f" usuario creado correctamente"}), 201

# Ruta para crear un dato nuevo
@post_routes.route('/crear_dato', methods=['POST'])
@verificar_token
#@verificar_token
def crear_dato():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos no proporcionados"}), 400
    # validar datos

    city = data.get("city")
    region = data.get("region")
    country= data.get("country")
    air_quality= data.get("air_quality")
    water_pollution= data.get("water_pollution")
    if not city or not region or not country or not air_quality or not water_pollution:
        return jsonify({"error": "faltan datos para crear el usuario"}), 400
    # Llama a la función create_role para crear el rol en Supabase
    result = crud.create_data(data)
    if isinstance(result, Exception):
        return jsonify({"error": str(result)}), 500
    
    new_data = [[air_quality, water_pollution]]
    response = predictor.get_prediction_text(predictor.get_prediction(new_data))

    return response
