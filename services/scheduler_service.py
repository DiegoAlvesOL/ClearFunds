import json
import os.path
from datetime import timedelta, datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "../data/scheduled_payments.json")
BASE_DIR_TRANSACTION = os.path.dirname(os.path.abspath(__file__))
FILE_PATH_TRANSACTION = os.path.join(BASE_DIR_TRANSACTION, "../data/transactions.json")

def load_trasactions():
    if os.path.exists(FILE_PATH_TRANSACTION):
        with open(FILE_PATH_TRANSACTION, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def load_scheduled_payments():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def calculate_fee (transaction):
    fee_rate = transaction.get("fee_rate",0)
    total_amount = transaction.get("total_amount",0)

    fee_amount = total_amount * (fee_rate/100)
    net_amount = total_amount - fee_amount

    return {
        "fee_amount": round(fee_amount,2),
        "net_amount": round(net_amount,2)
    }

def generate_date(transaction):
    global days_to_add
    transaction_type = transaction.get("transaction_type")
    transaction_date_str = transaction.get("transaction_datetime")

    transaction_date = datetime.strptime(transaction_date_str, "%d-%m-%Y %H:%M:%S")



    if transaction_type == "credit":
        days_to_add = 30
    elif transaction_type == "debit":
        days_to_add = 2

    payment_date = transaction_date + timedelta(days=days_to_add)
    return payment_date.strftime("%Y-%m-%d")


def generate_payment_schedule():
    scheduled = load_scheduled_payments()
    transactions = load_trasactions()

    scheduled_ids = []

    for item in scheduled:
        scheduled_ids.append(item.get("transaction_id"))

    new_schedules = []

    for transaction in transactions:
        if transaction.get("transaction_id") not in scheduled_ids:
            calculate = calculate_fee(transaction)

            scheduled = {
                "transaction_id": transaction["transaction_id"],
                "mti": transaction["mti"],
                "transaction_type": transaction["transaction_type"],
                "merchant_id": transaction["merchant_id"],
                "transaction_datetime": transaction["transaction_datetime"],
                "total_amount": transaction["total_amount"],
                "instalment_count": transaction["instalment_count"],
                "instalment_amount": transaction["instalment_amount"],
                "bin": transaction["bin"],
                "brand": transaction["brand"],
                "fee_amount": calculate["fee_amount"],
                "net_amount": calculate["net_amount"],
                "payment_date": generate_date(transaction)
            }
            new_schedules.append(scheduled)
    save_schedule(new_schedules)

def save_schedule(new_schedules):
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                exist_schedule = json.load(file)
            except json.JSONDecodeError:
                exist_schedule = []

    else:
        exist_schedule = []
    for schedule in new_schedules:
        exist_schedule.append(schedule)

    with open(FILE_PATH, "w") as file:
        json.dump(exist_schedule, file, indent=4)