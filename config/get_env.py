from dotenv import dotenv_values

config = dotenv_values(".env")

print(config)
BACKEND_URL = config['BACKEND_URL']