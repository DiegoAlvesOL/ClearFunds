import json
import os.path
import random
import string

# Define os caminhos para os arquivos JSON utilizados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR,"../data/merchants.json")

# Carrega todos os merchants cadastrados
def load_merchant():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Verifica se já existe um merchant com o company_number informado
def merchant_exists(company_number):
    merchants =load_merchant()
    return any (merchant.get("company_number") == company_number for merchant in merchants)

# Gera um ID único para o merchant com prefixo 'CF-'
def generate_id():
    letter_digits_id = string.ascii_uppercase + string.digits

    id_for_merchant = ""
    prefix = "CF-"
    for i in range(10):
        id_for_merchant = id_for_merchant + random.choice(letter_digits_id)
    return prefix + id_for_merchant

# Salva um novo merchant no arquivo merchants.json
def save_merchant(merchant_obj):
    merchant_data = merchant_obj.to_dict()

    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                merchants = json.load(file)
            except json.JSONDecodeError:
                merchants = []

    else:
        merchants = []

    merchants.append(merchant_data)

    with open(FILE_PATH, "w") as file:
        json.dump(merchants,file, indent=4)