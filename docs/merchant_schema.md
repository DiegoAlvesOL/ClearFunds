# Merchant Fields Documentation

This document describes the structure and purpose of each field used to register a merchant in the ClearFund platform.

---

## Field Name: `id_CF`
**Description:** Unique internal identifier for the merchant in the ClearFund platform.  
**Format:** Numeric value (manual entry)  
**Example:** `101`  
**Type:** `str`

---

## Field Name: `company_name`
**Description:** Legal name of the company or merchant.  
**Format:** Title-case string  
**Examples:**
- `"ClearFunds Ltd."` (🇮🇪 Ireland)
- `"AlphaTech Soluções LTDA"` (🇧🇷 Brazil)  
  **Type:** `str`

---

## Field Name: `company_number`
**Description:** Company’s official registration number.  
**Format:** Numeric, no punctuation  
**Examples:**
- `12345678000199` (CNPJ – 🇧🇷 Brazil)
- `635274` (Company Registration Number – 🇮🇪 Ireland)  
  **Type:** `int`

---

## Field Name: `vat_number`
**Description:** VAT or tax-related ID used in the country of operation.  
**Format:** Uppercase alphanumeric  
**Examples:**
- `"BR123456789"` (🇧🇷 Brazil – CNPJ format)
- `"IE6388047V"` (🇮🇪 Ireland – Irish VAT Number)  
  **Type:** `str`

---

## Field Name: `debit_fee`
**Description:** Percentage fee to apply on **debit transactions**.  
**Format:** Decimal value  
**Example:** `0.015` (means 1.5%)  
**Type:** `float`

---

## Field Name: `credit_fee`
**Description:** Percentage fee to apply on **credit transactions**.  
**Format:** Decimal value  
**Example:** `0.025` (means 2.5%)  
**Type:** `float`

---

## Field Name: `bank_info`
**Description:** Bank account information where funds will be settled.  
**Format:** Alphanumeric string (bank name, account and branch)  
**Examples:**
- `"AIB – IBAN IE29AIBK93115212345678"` (🇮🇪 Ireland)
- `"Banco do Brasil – Ag. 1234, Cc. 56789-0"` (🇧🇷 Brazil)  
  **Type:** `str`

---

> 🛑 **Note:** The previously used field `fee_rate` has been deprecated. It was replaced with `debit_fee` and `credit_fee` to provide more accurate fee control by payment type.
