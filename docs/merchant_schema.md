# Merchant Fields Documentation

## Field Name: company_name
**Description:** Legal name of the company or merchant.  
**Format:** Title case string (e.g., "AlphaTech Solutions LTDA")  
**Type:** str

## Field Name: company_number
**Description:** Unique identifier for the company (e.g., CNPJ, registration number).  
**Format:** Numeric (no punctuation)  
**Example:** 12345678000199  
**Type:** int

## Field Name: vat_number
**Description:** VAT (Value-Added Tax) number or similar tax-related ID depending on jurisdiction.  
**Format:** Alphanumeric string  
**Type:** str

## Field Name: fee_rate
**Description:** Fee rate (%) applied to each transaction performed by the merchant.  
**Format:** Decimal value (e.g., 2.5 means 2.5%)  
**Type:** float

## Field Name: bank_info
**Description:** Bank account information where funds will be settled.  
**Format:** Alphanumeric string (can include agency and account number)  
**Example:** "Banco do Brasil – Ag. 1234, Cc. 56789-0"  
**Type:** str

## Field Name: merchant_id
**Description:** Unique ID used internally by the platform to identify the merchant.  
**Format:** UUID or alphanumeric  
**Type:** str
