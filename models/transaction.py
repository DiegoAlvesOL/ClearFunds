class Transaction:
    def __init__(self,transaction_id,
                 mti,
                 transaction_type,
                 transaction_datetime,
                 terminal_id,
                 nsu,
                 auth_code,
                 currency_code,
                 total_amount,
                 merchant_id,
                 company_number,
                 mcc,
                 fee_rate,
                 instalment_count,
                 instalment_amount,
                 bin,
                 brand,
                 original_data ):
        self.transaction_id = transaction_id
        self.mti = mti
        self.transaction_type = transaction_type
        self.transaction_datetime = transaction_datetime
        self.terminal_id = terminal_id
        self.nsu = nsu
        self.auth_code = auth_code
        self.currency_code = currency_code
        self.total_amount = total_amount
        self.merchant_id = merchant_id
        self.company_number = company_number
        self.mcc = mcc
        self.fee_rate = fee_rate
        self.instalment_count = instalment_count
        self.instalment_amount = instalment_amount
        self.bin = bin
        self.brand = brand
        self.original_data = original_data

    # Converte o objeto Transaction em um dicionário (Usado para savar os arquivos .JSON)
    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "mti": self.mti,
            "transaction_type": self.transaction_type,
            "transaction_datetime": self.transaction_datetime,
            "terminal_id": self.terminal_id,
            "nsu": self.nsu,
            "auth_code": self.auth_code,
            "currency_code": self.currency_code,
            "total_amount": self.total_amount,
            "merchant": {
                "merchant_id": self.merchant_id,
                "company_number": self.company_number,
                "mcc": self.mcc,
                "fee_rate": self.fee_rate,
            },
            "instalment_info": {
                "instalment_count": self.instalment_count,
                "instalment_amount": self.instalment_amount,
            },
            "card_info":{
                "bin": self.bin,
                "brand": self.brand,
            },
            "original_data": self.original_data
        }