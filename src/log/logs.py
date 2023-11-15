import logging

class Logs:
    file_handler = None

    def __init__(self):
        # Configura la ubicación completa del archivo de registros
        log_file = 'src/log/app.log'

        # Crea un manejador de archivo para escribir los registros en el archivo
        self.file_handler = logging.FileHandler(log_file)

        # Configura el nivel de registro y el formato
        self.file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(formatter)

    def get_file_handler(self):
        return self.file_handler