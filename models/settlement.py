class SettlementPayment:
    def __init__(self, transaction_id, mti, transaction_type, merchant_id, transaction_datetime,
                 total_amount, instalment_count, instalment_amount, bin, brand, fee_amount,
                 net_amount, payment_date, status):
        self.transaction_id = transaction_id
        self.mti = mti
        self.transaction_type = transaction_type
        self.merchant_id =merchant_id
        self.transaction_datetime = transaction_datetime
        self.total_amount = total_amount
        self.instalment_count = instalment_count
        self.instalment_amount = instalment_amount
        self.bin = bin
        self.brand = brand
        self.fee_amount = fee_amount
        self.net_amount = net_amount
        self.payment_date = payment_date
        self.status = status

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "mti": self.mti,
            "transaction_type": self.transaction_type,
            "merchant_id": self.merchant_id,
            "transaction_datetime": self.transaction_datetime,
            "total_amount": self.total_amount,
            "instalment_count": self.instalment_count,
            "instalment_amount": self.instalment_amount,
            "bin": self.bin,
            "brand": self.brand,
            "fee_amount": self.fee_amount,
            "net_amount": self.net_amount,
            "payment_date": self.payment_date,
            "status": self.status
        }