import json
import os.path
import random
import string

# Define os caminhos para os arquivos JSON utilizados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "../data/transactions.json")
BASE_DIR_UNLINKED = os.path.dirname(os.path.abspath(__file__))
FILE_PATH_UNLINKED = os.path.join(BASE_DIR_UNLINKED, "../data/transaction_unlinked.json")
BASE_DIR_MERCHANT = os.path.dirname(os.path.abspath(__file__))
FILE_PATH_MERCHANT = os.path.join(BASE_DIR_MERCHANT,"../data/merchants.json")
BASE_DIR_BIN = os.path.dirname(os.path.abspath(__file__))
FILE_PATH_BIN = os.path.join(BASE_DIR_BIN, "../data/card_bin.json")

# Carrega todos os merchants salvos no arquivo merchants.json
def load_merchants():
    if os.path.exists(FILE_PATH_MERCHANT):
        with open(FILE_PATH_MERCHANT, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

#Carrega a base de bin e bandeiras para função que valida qual é o bandeira correta apartir do bin informado.
def load_card_bin():
    if os.path.exists(FILE_PATH_BIN):
        with open(FILE_PATH_BIN, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Retorna o merchant com base no ID (id_CF)
def get_merchant_by_id(merchant_id):
    merchants = load_merchants()
    for merchant in merchants:
        if merchant.get("id_CF") == merchant_id:
            return merchant
    return None

def generate_id_transaction_id ():
    letter_digits_id = string.ascii_uppercase + string.digits

    id_for_transaction = ""
    prefix_id = "CF"

    for prefix in range (12):
        id_for_transaction = id_for_transaction + random.choice(letter_digits_id)

    return prefix_id + id_for_transaction


def infer_card_brand_from_bin(bin):
    bin_data = load_card_bin()
    transaction_bin = bin[:6]

    for entry in bin_data:
        if entry.get("bin") == transaction_bin:
            return entry.get("brand")
    return "Unknown"


# Processa uma transação recebida (verifica merchant, aplica fee, salva transação)
def process_transaction(transactio_obj):
    transaction_data = transactio_obj.to_dict()
    merchant_id = transaction_data.get("merchant",{}).get("merchant_id")

    merchant = get_merchant_by_id(merchant_id)


    if merchant:
        transaction_data["merchant"]["merchant_id"] = merchant.get("id_CF")
        payment_type = transaction_data.get("transaction_type")

        if payment_type == "credit":
            transaction_data["merchant"]["fee_rate"] = merchant.get("credit_fee")
        elif payment_type == "debit":
            transaction_data["merchant"]["fee_rate"] = merchant.get("debit_fee")
        else:
            save_transaction_unlinked(transaction_data)
            return

        save_transaction(transaction_data)

    else:
        save_transaction_unlinked(transaction_data)

# Salva transações válidas no arquivo transactions.json
def save_transaction(transaction_data):
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH,"r") as file:
            try:
                transactions = json.load(file)
            except json.JSONDecodeError:
                transactions = []

    else:
        transactions = []
    transactions.append(transaction_data)

    with open(FILE_PATH, "w") as file:
        json.dump(transactions, file, indent=4)

# Salva transações que não puderam ser vinculadas a um merchant no arquivoo transaction_unlinked.json
def save_transaction_unlinked(transaction_data):
    if os.path.exists(FILE_PATH_UNLINKED):
        with open(FILE_PATH_UNLINKED,"r") as file:
            try:
                transactions_unlinked = json.load(file)
            except json.JSONDecodeError:
                transactions_unlinked = []
    else:
        transactions_unlinked = []
    transactions_unlinked.append(transaction_data)

    with open(FILE_PATH_UNLINKED, "w") as file:
        json.dump(transactions_unlinked, file, indent=4)