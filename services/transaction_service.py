import json
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "../data/transactions.json")



def save_transaction(transaction_obj):
    transaction_data = transaction_obj.to_dict()

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



