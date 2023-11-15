from functools import wraps
from flask import request, jsonify
import jwt
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

secret_key = os.getenv("SECRET_KEY")

def verificar_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'mensaje': 'Token no proporcionado'}), 401

        if token.startswith('Bearer '):
            token = token[7:]

        try:
            data = jwt.decode(token, secret_key, algorithms=['HS256'])
            return func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({'mensaje': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'mensaje': 'Token no válido'}), 401

    return wrapper
