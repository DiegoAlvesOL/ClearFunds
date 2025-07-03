# Transaction Schema – ClearFund

This document describes the structure and purpose of each field used to register a transaction within the ClearFund platform. The model is inspired by [ISO 8583](https://en.wikipedia.org/wiki/ISO_8583), a standard used in electronic payment systems.

> 📘 **Standards Notice**  
> This document references international standards such as ISO 8583, ISO 8601, ISO 4217, and ISO 18245.  
> While official documentation is available via [iso.org](https://www.iso.org/), access is typically paid.  
> For educational and integration purposes, this schema uses trusted open-access references (e.g., Wikipedia).  
> These are sufficient for development and testing, but production implementations should consult official ISO specs.

---
## Field Summary Table

| Field                 | Source / Origin             | Notes                                                                 |
|-----------------------|------------------------------|-----------------------------------------------------------------------|
| `transaction_id`      | Provided by integrator       | Unique identifier (ClearFund standard)                                |
| `mti`                 | Provided by integrator       | ISO 8583 transaction type                                             |
| `transaction_type`    | Provided by integrator       | "debit" or "credit"                                                   |
| `transaction_datetime`| Provided by integrator       | ISO 8601 format                                                        |
| `terminal_id`         | Provided by integrator       | Origin terminal ID                                                    |
| `nsu`                 | Provided by integrator       | Acquirer transaction reference                                        |
| `auth_code`           | Provided by acquirer         | Code confirming transaction approval                                  |
| `currency_code`       | Provided by integrator       | ISO 4217 3-digit numeric code                                          |
| `total_amount`        | Provided by integrator       | Full value of the transaction                                         |
| `merchant_id`         | Provided by integrator       | Must follow "CF-" + 12 alphanumeric chars                             |
| `company_number`      | Provided by integrator       | Legal registration number (e.g., CNPJ or CRN)                         |
| `mcc`                 | Provided by integrator       | Merchant Category Code (numeric)                                      |
| `fee_rate`            | System-defined               | **Must NOT be sent by integrator**                                    |
| `instalment_count`    | Provided by integrator       | Number of instalments                                                 |
| `instalment_amount`   | Provided or calculated       | Amount charged per instalment                                         |
| `bin`                 | Provided or enriched         | First 6 digits + masked card (e.g., 123456******1212)                 |
| `brand`               | Provided by integrator       | Will be validated or overwritten based on BIN                         |
| `original_data`       | Provided by integrator       | Used in reversal/refund operations                                    |

---

## Core Transaction Data

### Field: `transaction_id`
**Description:**  
ClearFund's internal ID to uniquely identify the transaction.  
**Format:** Alphanumeric string starting with `"CF"`  
**Example:** `"CF1234567890"`  
**Note:** Replaces the traditional STAN (System Trace Audit Number).

---

### Field: `mti`
**Description:**  
Message Type Indicator (MTI) from [ISO 8583](https://en.wikipedia.org/wiki/ISO_8583#Message_Type_Indicator). Defines the nature of the transaction message.  
**Format:** 4-digit numeric string  
**Examples:**
- `0200`: Financial transaction request
- `0220`: Financial transaction response
- `0420`: Reversal request
- `0430`: Reversal response
- `0800`: Network management request

---

### Field: `transaction_type`
**Description:**  
Defines the payment method used by the customer.  
**Allowed Values:**
- `"debit"` – Paid from checking/balance
- `"credit"` – Paid via credit issuer  
  **Note:** In reversal/refund, this field must reflect the **original** payment method.

---

### Field: `transaction_datetime`
**Description:**  
Date and time of the transaction in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.  
**Example:** `"2025-06-01 15:30:00"`  
**Purpose:** Timestamp used for reconciliation and payment scheduling.

---

### Field: `terminal_id`
**Description:**  
Code identifying the terminal or system that submitted the transaction.  
**Example:** `"ABC12345"`

---
### Field: `nsu`
**Description:**  
Unique transaction ID assigned by the acquirer.  
**Purpose:** Used for reconciliation with external processors.

---

### Field: `auth_code`
**Description:**  
Approval code returned by the card network.  
**Type:** `str` (up to 6 characters)  
**Example:** `"A1B2C3"`

---

### Field: `currency_code`
**Description:**  
3-digit numeric code representing the transaction currency.  
**Format:** `str`  
**Examples:**
- 🇧🇷 `986` – BRL (Brazilian Real)
- 🇮🇪 `978` – EUR (Euro – Ireland)
- 🇪🇺 `978` – EUR (Euro – European Union)
- 🇺🇸 `840` – USD (United States Dollar)  
  **Reference:** [ISO 4217 – Currency Codes](https://en.wikipedia.org/wiki/ISO_4217)

---

### Field: `total_amount`
**Description:**  
Full transaction value in the original currency.  
**Type:** `float`  
**Example:** `300.00`

---
## 🧾 Merchant Information

### Field: `merchant_id`
**Description:**  
Unique identifier assigned by ClearFund to the registered merchant.  
**Format:** `"CF-"` + 12 alphanumeric characters  
**Example:** `"CF-P6ON34OOW4"`  

---

### Field: `company_number`
**Description:**  
Official business registration number of the merchant.  
**Format:** Numeric only, without punctuation  
**Examples:**
- 🇧🇷 `12345678000199` (CNPJ – Brazil)
- 🇮🇪 `635274` (Company Registration Number – Ireland)

---

### Field: `mcc`
**Description:**  
Merchant Category Code (MCC) representing the type of business.  
**Type:** `int` (must be numeric, 4 digits)  
**Example:** `5411`  
**Reference:** [ISO 18245 – MCC Documentation](https://en.wikipedia.org/wiki/Merchant_category_code)

---
### Field: `fee_rate`
**Description:**  
Fee percentage applied based on merchant and brand profile.  
**Type:** `float`  
**Example:** `2.5`  
**Important:** **This field must not be provided by the integrator.** It is managed internally by ClearFund and used for fee calculation.

---

## 💳 Instalment Informations

### Field: `instalment_count`
**Description:**  
Number of instalments requested by the customer.  
**Type:** `int`  
**Example:** `3`

---

### Field: `instalment_amount`
**Description:**  
Amount charged per instalment. Can be calculated as `total_amount ÷ instalment_count`.  
**Type:** `float`  
**Example:** `100.00`

---
## 💳 Card Information

### Field: `bin`
**Description:**  
First six digits of the card used, followed by masked characters.  
**Example:** `"453958******1212"`  
**Type:** `str`  
**Purpose:** Used to infer the `brand` and apply specific business rules.  
**Security Note:** BINs are not sensitive data but must be handled securely.  
For real-world implementations, compliance with [PCI DSS (Payment Card Industry Data Security Standard)](https://www.pcisecuritystandards.org/) is essential.

---

### Field: `brand`
**Description:**  
Card brand associated with the transaction.  
**Examples:** `"visa"`, `"mastercard"`, `"elo"`  
**Type:** `str`  
**Note:**  
Although this field should be provided by the integrator, ClearFund **will validate and, if needed, update it based on the `bin`** to ensure consistency with fee rules and settlement logic.

---

### Field: `original_data`
**Description:**  
References the `transaction_id` of the original transaction for reversals or refunds.  
**Type:** `str`  
**Example:** `"CF1234567890"`

---

## 🛑 Removed Fields

| Field               | Reason for Removal                                                                                                                                    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cf_transaction_id` | Replaced by `transaction_id`, which inherits STAN logic and serves as the primary identifier on the ClearFund platform, according to ISO 8583 logic. |
| `rrn`               | Redundant with `stan` and `auth_code`.                                                                                                                |
| `fees`              | Fees will be dynamically derived from the registered merchant profile.                                                                                |
| `settlement_date`   | Settlement will be calculated based on business rules (e.g., D+2 for debit, D+30 for credit).                                                         |

---

## 📎 Related Files

- `models/transaction.py`
- `services/transaction_service.py`
- `tests/test_transactions.py`
- `docs/schedule_schema.md`
- `docs/merchant_schema.md`
