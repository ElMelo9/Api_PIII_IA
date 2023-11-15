from flask import Flask
from flask_cors import CORS
import logging
from src.log.logs import Logs
from src.routes.getRoutes import get_routes
from src.routes.postRoutes import post_routes

logs = Logs()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

# Configura el logger de la aplicación para escribir en el archivo de registro
app.logger.addHandler(logs.get_file_handler())

# Configura el nivel de registro del logger de la aplicación
app.logger.setLevel(logging.DEBUG)

# Registra las rutas GET
app.register_blueprint(get_routes)

# Registra las rutas POST
app.register_blueprint(post_routes)

if __name__ == '__main__':
    app.run(port=4000, debug=True)
