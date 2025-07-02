import json
import os.path
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR,"../data/settled_payments.json")
BASE_DIR_SCHEDULED = os.path.dirname(os.path.abspath(__file__))
FILE_PATH_SCHEDULED = os.path.join(BASE_DIR_SCHEDULED,"../data/scheduled_payments.json")

def load_schedule():
    if os.path.exists(FILE_PATH_SCHEDULED):
        with open(FILE_PATH_SCHEDULED, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def load_settled():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Filtrar os pagamentos da lista cujo campo "payment_date" é igual à data de hoje.
def filter_payments_due_today(payments):
    today = date.today().isoformat()
    due_today = []

    for payment in payments:
        if payment.get("payment_date") <= today:
            due_today.append(payment)

    return due_today

def convert_to_settled(payment):
    settled_payment = payment.copy()
    settled_payment["status"] = "settled"
    return settled_payment

def save_settled(new_settlements):
    existing = load_settled()

    for payment in new_settlements:
        existing.append(payment)

    with open(FILE_PATH, "w") as file:
        json.dump(existing, file, indent=4)

def remove_settled_from_schedule(all_scheduled, settled):
    settled_ids = [payment["transaction_id"] for payment in settled]
    remaining =[]

    for payment in all_scheduled:
        if payment ["transaction_id"] not in settled_ids:
            remaining.append(payment)
    return remaining


def run_settlement_process():
    # carrega todos os pagamentos agendados
    scheduled_payments = load_schedule()

    # carrega dos os pagamentos já liquidados
    existing_settled = load_settled()

    # filtra os pagamentos q devem ser liquidados
    due_today = filter_payments_due_today(scheduled_payments)

    if not due_today:
        print("No payments scheduled for today")
        return

    # Converte os pagamentos em objetos liquidados
    new_settlements = []
    for payment in due_today:
        settled = convert_to_settled(payment)
        new_settlements.append(settled)

    # Salva os novos pagamentos no arquivo de transações liquidadas
    save_settled(new_settlements)

    updated_scheduled = remove_settled_from_schedule(scheduled_payments, new_settlements)

    with open(FILE_PATH_SCHEDULED, "w") as file:
        json.dump(updated_scheduled, file, indent=4)

    print("Total of Payments settled {}".format(len(new_settlements)))
