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

## Field: `transaction_type`
**Description:** Defines the payment modality of the transaction – debit or credit.  
**Format:** Lowercase string  
**Type:** str  
**Purpose:** Used to apply specific business logic, such as installment rules and fee calculations.  
**Allowed Values:**
- `"debit"` – Transaction made using a debit method.
- `"credit"` – Transaction made using a credit method.  
  **Important:** For reversal or refund operations, this field must reflect the **original payment type** (e.g., `"credit"` for a reversed credit sale).  
  **Example:** `"debit"`

---

## 🧾 Merchant Information

### Field: `merchant_id`
**Description:** Unique identifier of the merchant provided by the integration platform.  
**Format:** UUID or alphanumeric string  
**Type:** str  
**Purpose:** Links the transaction to the merchant previously registered in ClearFund.

### Field: `company_number`
**Description:** Company’s official registration number.  
**Format:** Numeric, no punctuation  
**Examples:**
- 🇧🇷 `12345678000199` (CNPJ – Brazil)
- 🇮🇪 `635274` (Company Registration Number – Ireland)  
  **Type:** int

### Field: `mcc`
**Description:** Merchant Category Code representing the merchant's business activity.  
**Format:** 4-digit string (e.g., "5411")  
**Type:** str  
**Purpose:** Business classification according to ISO 18245 (e.g., 5411 = grocery stores).

### Field: `terminal_id`
**Description:** Identifier of the terminal (POS/gateway/TEF) that processed the transaction.  
**Format:** Alphanumeric string (e.g., "ABC12345")  
**Type:** str  
**Purpose:** Identifies the origin terminal of the transaction.

---

## 💳 Transaction Details

### Field: `transaction_datetime`
**Description:** Date and time when the transaction occurred.  
**Format:** ISO 8601 string (e.g., "2025-05-24T14:30:00Z")  
**Type:** str  
**Purpose:** Timestamp of transaction execution by the merchant.

### Field: `stan`
**Description:** System Trace Audit Number – sequential identifier for the transaction.  
**Format:** Integer up to 6 digits (e.g., 123456)  
**Type:** int  
**Purpose:** Unique tracking number following ISO 8583.

### Field: `nsu`
**Description:** Unique transaction number provided by the acquirer.  
**Format:** Alphanumeric string  
**Type:** str  
**Purpose:** External identifier for transaction reconciliation (acquirer-level).

### Field: `auth_code`
**Description:** Authorization code returned by the acquiring network.  
**Format:** Alphanumeric string (up to 6 characters)  
**Type:** str  
**Purpose:** Confirms transaction approval.

### Field: `currency_code`
**Description:** Numeric currency code used in the transaction.  
**Format:** 3-digit string (e.g., "986" for BRL)  
**Type:** str  
**Purpose:** Currency used, in accordance with [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html).  
**Examples:**
- 🇧🇷 `986` – BRL (Brazilian Real)
- 🇮🇪 `978` – EUR (Euro – Ireland)
- 🇪🇺 `978` – EUR (Euro – European Union)
- 🇺🇸 `840` – USD (United States Dollar)

### Field: `total_amount`
**Description:** Total amount of the transaction.  
**Format:** Decimal (e.g., 300.00)  
**Type:** float  
**Purpose:** Full transaction value.

### Field: `fee_rate`
**Description:** Fee percentage rate applied to the transaction amount.  
**Format:** Decimal (e.g., 2.5 for 2.5%)  
**Type:** float  
**Purpose:** Used to calculate the transaction fee according to the merchant's pricing profile.

---

## 🧾 Instalment Information

### Field: `instalment_count`
**Description:** Number of installments for the transaction.  
**Format:** Integer ≥ 1  
**Type:** int  
**Purpose:** Indicates how many parts the amount was split into.

### Field: `instalment_amount`
**Description:** Value of each installment.  
**Format:** Decimal (e.g., 100.00)  
**Type:** float  
**Purpose:** Installment amount charged to the customer.

---

## 🔁 Auxiliary Fields

### Field: `original_data`
**Description:** Reference to the original transaction (used in refunds/cancellations).  
**Format:** Integer (e.g., 123456)  
**Type:** int  
**Purpose:** Should contain the `stan` of the original sale transaction.

---

## 🛑 Removed Fields

| Field               | Reason for Removal                                                                 |
|---------------------|-------------------------------------------------------------------------------------|
| `cf_transaction_id` | Replaced by `stan`, which already serves as a unique identifier and follows ISO 8583. |
| `rrn`               | Redundant with `stan` and `auth_code`.                                              |
| `fees`              | Fees will be dynamically derived from the registered merchant profile.              |
| `settlement_date`   | Settlement will be calculated based on business rules (e.g., D+2 for debit, D+30 for credit). |
