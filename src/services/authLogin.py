import os
import sys
# Obtén la ruta del directorio actual
current_directory = os.path.dirname(os.path.realpath(__file__))
# Agrega el directorio raíz de tu proyecto al sys.path
project_directory = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.append(project_directory)
from database.crud_operations import Crud

class AuthUser:
    crud = None
    data = None

    def __init__(self):
        self.crud = Crud()
        self.data = self.crud.get_users()

    def validate_credentials(self,email,password):
        
        for user in self.data:
            if user['email_user'] == email and user['password_user'] == password:
                return True
        return False

