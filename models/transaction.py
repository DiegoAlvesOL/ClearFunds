class Transaction:
    def __init__(self,mti,
                 transaction_datetime,
                 stan,
                 settlement_date,
                 mcc,
                 rrn,
                 auth_code,
                 terminal_id,
                 merchant_id,
                 currency_code,
                 original_data,
                 fees,
                 cf_transaction_id,
                 instalment_count,
                 instalment_amount ):
        self.mti = mti
        self.transaction_datatime = transaction_datetime
        self.stan = stan
        self.settlement_data = settlement_date
        self.mcc = mcc
        self.rrn = rrn
        self.auth_code = auth_code
        self.terminal_id = terminal_id
        self.merchant_id = merchant_id
        self.currency_code = currency_code
        self.original_data = original_data
        self.fees = fees
        self.cf_transaction_id = cf_transaction_id
        self.instalment_count = instalment_count
        self.instalment_amount = instalment_amount

    def to_dict(self):
        return {
            "mti": self.mti,
            "transaction_datatime": self.transaction_datatime,
            "stan": self.stan,
            "settlement_data": self.settlement_data,
            "mcc": self.mcc,
            "rrn": self.rrn,
            "auth_code": self.auth_code,
            "terminal_id": self.terminal_id,
            "merchant_id": self.merchant_id,
            "currency_code": self.currency_code,
            "original_data": self.original_data,
            "fees": self.fees,
            "cf_transaction_id": self.cf_transaction_id,
            "instalment_count": self.instalment_count,
            "instalment_amount": self.instalment_amount
        }
