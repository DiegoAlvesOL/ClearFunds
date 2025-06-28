# SettledPayment Fields Documentation

This document describes the structure and purpose of each field generated in the settlement phase of the ClearFunds platform.

Settled payments represent transactions that have reached their due date and have been processed for payment to the merchant, with all fees calculated and applied.

---

## Field Summary Table

| Field                  | Source / Origin             | Notes                                                                 |
|------------------------|-----------------------------|-----------------------------------------------------------------------|
| `transaction_id`       | From scheduled payment       | Used to trace back to the transaction                                 |
| `mti`                  | Inherited from schedule      | Useful for filtering or auditing                                      |
| `transaction_type`     | Inherited from schedule      | e.g., credit, debit                                                   |
| `merchant_id`          | Inherited from schedule      | Merchant receiving the payment                                        |
| `transaction_datetime` | Inherited from schedule      | Retained for tracking and auditability                               |
| `total_amount`         | Inherited from schedule      | Full transaction value                                                |
| `instalment_count`     | Inherited from schedule      | Number of instalments (if applicable)                                 |
| `instalment_amount`    | Inherited from schedule      | Value per instalment                                                  |
| `bin`                  | Inherited from schedule      | Used for card brand identification                                    |
| `brand`                | Inherited from schedule      | e.g., Visa, Mastercard                                                |
| `fee_amount`           | Inherited from schedule      | Fee calculated at the time of scheduling                              |
| `net_amount`           | Inherited from schedule      | Final amount to be paid to merchant                                   |
| `payment_date`         | Inherited from schedule      | Date when the payment was scheduled to occur                          |
| `status`               | Defined in settlement phase  | Always set to `"settled"` during settlement                           |

---

## Field Details

### Field: `transaction_id`
**Description:** Unique identifier referencing the original transaction.  
**Source:** `scheduled_payments.json`  
**Type:** `str`  
**Example:** `"CFU3Z1NIC292WO"`

---

### Field: `mti`
**Description:** Message Type Indicator used in ISO 8583 messaging, representing the type of transaction.  
**Inherited from:** scheduled payment  
**Type:** `str`  
**Example:** `"0200"`

---

### Field: `transaction_type`
**Description:** Specifies the type of the transaction, typically `"credit"` or `"debit"`.  
**Inherited from:** scheduled payment  
**Type:** `str`  
**Example:** `"credit"`

---

### Field: `merchant_id`
**Description:** Unique ID of the merchant receiving the payment.  
**Inherited from:** scheduled payment  
**Type:** `str`  
**Example:** `"CF-N6IDB58K49"`

---

### Field: `transaction_datetime`
**Description:** Date and time when the transaction occurred.  
**Purpose:** Retained for auditing and future reporting.  
**Type:** `str` (format: `dd-mm-yyyy HH:MM:SS`)  
**Example:** `"17-06-2025 10:23:03"`

---

### Field: `total_amount`
**Description:** Full value of the transaction.  
**Type:** `float`  
**Example:** `460.00`

---

### Field: `instalment_count`
**Description:** Total number of instalments associated with the transaction.  
**Type:** `int`  
**Example:** `1`

---

### Field: `instalment_amount`
**Description:** Value of each instalment.  
**Inherited from:** schedule logic  
**Type:** `float`  
**Example:** `460.00`

---

### Field: `bin`
**Description:** First 6–8 digits of the card used (masked).  
**Purpose:** Used to identify card brand and for reporting analytics.  
**Type:** `str`  
**Example:** `"5436********5072"`

---

### Field: `brand`
**Description:** Card brand (e.g., Visa, Mastercard), derived from the BIN.  
**Type:** `str`  
**Example:** `"MasterCard"`

---

### Field: `fee_amount`
**Description:** Fee amount calculated during the scheduling phase.  
**Formula:** `total_amount * fee_percentage`  
**Type:** `float`  
**Example:** `8.74`

---

### Field: `net_amount`
**Description:** Final amount transferred to the merchant.  
**Formula:** `total_amount - fee_amount`  
**Type:** `float`  
**Example:** `451.26`

---

### Field: `payment_date`
**Description:** Date when this payment was scheduled to be settled.  
**Purpose:** Allows the system to trigger settlement when `payment_date == today`.  
**Type:** `str` (format: `yyyy-mm-dd`)  
**Example:** `"2025-07-17"`

---

### Field: `status`
**Description:** Represents the current status of the payment.  
**Default value:** `"settled"`  
**Defined in:** `SettledPayment` class within `settlement_service.py`  
**Type:** `str`  
**Example:** `"settled"`

---

## Use Cases & Insights (for future analytics)

By preserving this structure, ClearFunds enables:

- Aggregated views by brand (e.g., Mastercard total settled today)
- Merchant performance dashboards (e.g., top receivers by volume)
- Settlement reports by period, card type, or transaction type

---

## Related Files

- `models/settlement.py`
- `services/settlement_service.py`
- `data/settled_payments.json`
- `docs/schedule_schema.md`
- `docs/transaction_schema.md`
