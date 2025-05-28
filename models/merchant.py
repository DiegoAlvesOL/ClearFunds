

class Merchant:
    def __init__(self,id_CF, company_name, company_number, vat_number, debit_fee, credit_fee, bank_info):
        self.id_CF = id_CF
        self.company_name = company_name
        self.company_number = company_number
        self.vat_number = vat_number
        # self.fee_rate = fee_rate
        self.debit_fee = debit_fee
        self.credit_fee = credit_fee
        self.bank_info = bank_info

    def __str__(self):
        return "|"+str(self.id_CF) + "|" + self.company_name + "|" + str(self.company_number) + "|" + self.vat_number + "|" + str(self.debit_fee) + "|"+ str(self.credit_fee) + "|" + str(self.bank_info) + "|"


    def to_dict(self):
        return {
            "id_CF": self.id_CF,
            "company_name": self.company_name,
            "company_number": self.company_number,
            "vat_number": self.vat_number,
            # "fee_rate": self.fee_rate,
            "debit_fee": self.debit_fee,
            "credit_fee": self.credit_fee,
            "bank_info": self.bank_info
        }
