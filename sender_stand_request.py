import configuration
import requests
import data

# Crear un nuevo usuario
def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )

# Obtener la tabla de usuarios
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Buscar kits por productos (por si se requiere luego)
def post_products_kits(products_ids):
    return requests.post(
        configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
        json=products_ids,
        headers=data.headers
    )