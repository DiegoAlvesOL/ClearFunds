
import json
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR,"../data/merchants.json")

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
