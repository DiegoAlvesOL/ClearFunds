# Transaction Schema – ClearFund

This document describes the structure and purpose of each field used to register a transaction within the ClearFund platform. The model is inspired by ISO 8583, a standard used in electronic payment systems.

---

## Field: `mti`
**Description:** Message Type Indicator (MTI) based on ISO 8583 standard.  
**Format:** 4-digit numeric code (e.g., 0200, 0420)  
**Type:** int  
**Purpose:** Indicates the type of transaction message (e.g., purchase, reversal). Defined by ClearFund according to the operation.
**Example Values:**
- 0200: Financial transaction request
- 0220: Financial transaction response
- 0420: Reversal request
- 0430: Reversal response

---

## Field: `transaction_datetime`
**Description:** Date and time when the transaction occurred.  
**Format:** ISO 8601 string (e.g., "2025-05-24T14:30:00Z")  
**Type:** str  
**Purpose:** Represents the moment the transaction was performed by the merchant. Supplied by the platform integrated with ClearFund.

---

## Field: `stan`
**Description:** System Trace Audit Number (STAN), a sequential identifier for the transaction as defined in ISO 8583.  
**Format:** Integer up to 6 digits (e.g., 123456)  
**Type:** int  
**Purpose:** Unique sequential number to track the transaction. Supplied by the integrated platform (POS, gateway, or TEF).

---

## Field: `mcc`
**Description:** Merchant Category Code representing the merchant's business activity.  
**Format:** 4-digit string (e.g., "5411")  
**Type:** str  
**Purpose:** Business classification according to ISO 18245 (e.g., 5411 = grocery stores). Supplied by the integrated platform.

---

## Field: `auth_code`
**Description:** Authorization code returned by the acquiring network (e.g., Visa, Mastercard).  
**Format:** Alphanumeric string, up to 6 characters  
**Type:** str  
**Purpose:** Confirms transaction approval. Supplied by the platform integrated with the acquiring party.

---

## Field: `terminal_id`
**Description:** Identifier of the terminal (POS, gateway, or TEF) that processed the transaction.  
**Format:** Alphanumeric string (e.g., "ABC12345")  
**Type:** str  
**Purpose:** Identifies the physical or virtual terminal that originated the transaction. Supplied by the payment gateway or TEF provider.

---

## Field: `merchant_id`
**Description:** Unique identifier of the merchant.  
**Format:** UUID or alphanumeric string  
**Type:** str  
**Purpose:** Links the transaction to the merchant previously registered in ClearFund. Supplied by the integration platform or internal system.

---

## Field: `currency_code`
**Description:** Numeric currency code used in the transaction.  
**Format:** 3-digit string (e.g., "986" for BRL, "978" for EUR)  
**Type:** str  
**Purpose:** Indicates the currency in accordance with ISO 4217. Supplied by the integration platform.

---

## Field: `original_data`
**Description:** Reference to the original transaction in cases such as cancellations or refunds.  
**Format:** Integer (e.g., 123456)  
**Type:** int  
**Purpose:** Should contain the `stan` of the original sale transaction. Supplied by the integration platform.

---

## Field: `instalment_count`
**Description:** Number of installments for the transaction.  
**Format:** Integer ≥ 1  
**Type:** int  
**Purpose:** Indicates how many installments the total amount was split into. Supplied by the integration platform.

---

## Field: `instalment_amount`
**Description:** Amount of each installment.  
**Format:** Decimal (e.g., 100.00)  
**Type:** float  
**Purpose:** Value charged in each installment. Supplied by the integration platform.

---

## Field: `total_amount`
**Description:** Total amount of the transaction (instalment_amount * instalment_count).  
**Format:** Decimal (e.g., 300.00)  
**Type:** float  
**Purpose:** Total value of the transaction. Supplied by the integration platform.

---

## 🛑 Removed Fields

| Field               | Reason for Removal                                                                 |
|---------------------|-------------------------------------------------------------------------------------|
| `cf_transaction_id` | Replaced by `stan`, which already serves as a unique identifier and follows ISO 8583. |
| `rrn`               | Redundant with `stan` and `auth_code`.                                              |
| `fees`              | Fees will be dynamically derived from the registered merchant profile.              |
| `settlement_date`   | Settlement will be calculated based on business rules (e.g., D+2 for debit, D+30 for credit). |
| `responsável`       | Subjective field with no technical need at this stage of transaction registration.   |
