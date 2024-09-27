import os 
from dotenv import load_dotenv

load_dotenv('.env.dev')

api_USER_NAME= os.getenv('USER_NAME')
API_KEY= os.getenv('API_KEY')
EMAIL= os.getenv('EMAIL')
DATABASE_URL= os.getenv('DATABASE_URL')


print(f"API user:{api_USER_NAME}")
print(f"API API_KEY:{API_KEY}")
print(f"API EMAIL:{EMAIL}")
print(f"API DATABASE_URL:{DATABASE_URL}")


