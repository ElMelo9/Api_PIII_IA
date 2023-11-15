from flask import Blueprint ,request, jsonify
import os
import sys
# Obtén la ruta del directorio actual
current_directory = os.path.dirname(os.path.realpath(__file__))
# Agrega el directorio raíz de tu proyecto al sys.path
project_directory = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.append(project_directory)
import jwt 
from services.authToken import verificar_token
from database.crud_operations import Crud
crud = Crud()

get_routes = Blueprint('get_routes', __name__)

# Ruta para obtener todos los roles
@get_routes.route('/obtener_roles', methods=['GET'])
@verificar_token
def obtener_roles():
    # Realiza una consulta para obtener todos los roles
    response = crud.get_roles()
    print(response)

    return response


# Ruta para obtener todos los tipo de documentos
@get_routes.route('/obtener_tipoDoc', methods=['GET'])
@verificar_token
def obtener_tipoDoc():
    # Realiza una consulta para obtener todos los roles
    response = crud.get_tipoDoc()
    print(response)

    return response

# Ruta para obtener todos los usuarios
@get_routes.route('/obtener_usuarios', methods=['GET'])
@verificar_token
def obtener_users():
    # Realiza una consulta para obtener todos los roles
    response = crud.get_users()

    return response



# Ruta para obtener todos los datos nuevos
@get_routes.route('/obtener_datos', methods=['GET'])
@verificar_token
def obtener_datos():
    # Realiza una consulta para obtener todos los datos
    response = crud.get_data()

    return response

