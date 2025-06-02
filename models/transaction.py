class Transaction:
    def __init__(self,mti,
                 transaction_type,
                 merchant_id,
                 company_number,
                 mcc,
                 fee_rate,
                 terminal_id,
                 transaction_datetime,
                 stan,
                 nsu,
                 auth_code,
                 currency_code,
                 total_amount,
                 instalment_count,
                 instalment_amount,
                 original_data ):
        self.mti = mti
        self.transaction_type = transaction_type
        self.merchant_id = merchant_id
        self.company_number = company_number
        self.mcc = mcc
        self.fee_rate = fee_rate
        self.terminal_id = terminal_id
        self.transaction_datetime = transaction_datetime
        self.stan = stan
        self.nsu = nsu
        self.auth_code = auth_code
        self.currency_code = currency_code
        self.total_amount = total_amount
        self.instalment_count = instalment_count
        self.instalment_amount = instalment_amount
        self.original_data = original_data

    # Converte o objeto Transaction em um dicionário (Usado para savar os arquivos .JSON)
    def to_dict(self):
        return {
            "mti": self.mti,
            "transaction_type": self.transaction_type,
            "merchant_id": self.merchant_id,
            "company_number": self.company_number,
            "mcc": self.mcc,
            "fee_rate": self.fee_rate,
            "terminal_id": self.terminal_id,
            "transaction_datetime": self.transaction_datetime,
            "stan": self.stan,
            "nsu": self.nsu,
            "auth_code": self.auth_code,
            "currency_code": self.currency_code,
            "total_amount": self.total_amount,
            "instalment_count": self.instalment_count,
            "instalment_amount": self.instalment_amount,
            "original_data": self.original_data
        }
