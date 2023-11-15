import supabase
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

url = os.getenv("SUPABASE_URL")
api_key = os.getenv("SUPABASE_API_KEY")

supabase_client = supabase.create_client(url, api_key)

