# ScheduledPayment Fields Documentation

This document describes the structure and purpose of each field generated in the scheduled payment phase of the ClearFunds platform.

Scheduled payments are built after processing the original transactions, applying brand-specific fee rules, and calculating the appropriate payment date.

---

## Field Summary Table

| Field                  | Source / Origin             | Notes                                                                 |
|------------------------|-----------------------------|-----------------------------------------------------------------------|
| `transaction_id`       | Original transaction ID     | Used to trace back to the transaction                                 |
| `mti`                  | Inherited from transaction  | Useful for filtering or auditing                                      |
| `transaction_type`     | Inherited from transaction  | e.g., credit, debit                                                   |
| `merchant_id`          | Inherited from transaction  | Merchant receiving the payment                                        |
| `transaction_datetime` | Inherited from transaction  | Used to compute payment date (D+X rule)                               |
| `total_amount`         | Inherited from transaction  | Full transaction value                                                |
| `instalment_count`     | Inherited from transaction  | Number of instalments (if applicable)                                 |
| `instalment_amount`    | **Calculated**              | Derived from total_amount ÷ instalment_count                          |
| `bin`                  | Manually informed for test  | Used to derive the brand from BIN range                               |
| `brand`                | Derived from BIN            | e.g., Visa, Mastercard                                                |
| `fee_amount`           | Calculated via rule         | Based on percentage applied according to the brand                    |
| `net_amount`           | total_amount - fee_amount   | Final amount to be paid to merchant                                   |
| `payment_date`         | Calculated (D+X logic)      | Varies depending on transaction type (e.g., D+30 for credit)          |

---

## Field Details

### Field: `transaction_id`
**Description:** Unique identifier referencing the original transaction.  
**Source:** `transactions.json`  
**Type:** `str`  
**Example:** `"TXN0001"`

---

### Field: `mti`
**Description:** Message Type Indicator used in ISO 8583 messaging, representing the type of transaction.  
**Inherited from:** transaction  
**Type:** `str`  
**Example:** `"0200"`

---

### Field: `transaction_type`
**Description:** Specifies the type of the transaction, typically `"credit"` or `"debit"`.  
**Inherited from:** transaction  
**Type:** `str`  
**Example:** `"credit"`

---

### Field: `merchant_id`
**Description:** Unique ID of the merchant associated with the transaction.  
**Inherited from:** transaction  
**Type:** `str`  
**Example:** `"CF-BCMW1C8N2T"`

---

### Field: `transaction_datetime`
**Description:** Date and time when the transaction occurred.  
**Used for:** calculating payment date (D+X)  
**Type:** `str` (ISO 8601 format)  
**Example:** `"2024-06-01T15:30:00"`

---

### Field: `total_amount`
**Description:** Total amount of the transaction.  
**Type:** `float`  
**Example:** `150.00`

---

### Field: `instalment_count`
**Description:** Number of instalments agreed in the transaction.  
**Type:** `int`  
**Example:** `3`

---

### Field: `instalment_amount`
**Description:** Amount calculated for each instalment.  
**Logic:** Automatically computed as `total_amount ÷ instalment_count`, rounded to 2 decimals.  
In case of rounding differences, the last instalment is adjusted to match the `total_amount`.  
**Type:** `float`  
**Example:** `50.00`

---

### Field: `bin`
**Description:** First 6 digits of the card used in the transaction.  
**Purpose:** Used to derive the card brand.  
**Type:** `str`  
**Example:** `"453958"`

---

### Field: `brand`
**Description:** Card brand derived from the BIN.  
**Type:** `str`  
**Example:** `"visa"`

---

### Field: `fee_amount`
**Description:** Calculated fee amount based on brand-specific percentage.  
**Formula:** `total_amount * fee_percentage`  
**Type:** `float`  
**Example:** `2.25`

---

### Field: `net_amount`
**Description:** Net value to be paid to the merchant.  
**Formula:** `total_amount - fee_amount`  
**Type:** `float`  
**Example:** `147.75`

---

### Field: `payment_date`
**Description:** Scheduled payment date to the merchant.  
**Logic:** Based on transaction type:
- Debit: D+0
- Credit: D+30
- (In future updates, additional dates will be created per instalment count)  
  **Type:** `str` (ISO 8601)  
  **Example:** `"2024-07-01"`

---

## 🔐 Security Consideration

This system simulates part of a real-world payment processing environment. In actual implementations, **compliance with PCI DSS (Payment Card Industry Data Security Standard)** is essential to ensure secure handling of cardholder data.

While this project **does not store or process full card data**, it's important to understand that:

- Real systems **must not** store full PAN or sensitive authentication data.
- Card BINs (first 6 digits) can be used for analytics or routing but **should be handled securely**.
- Logging or exposing any trace of card data must follow **PCI-compliant practices**.

---

## Related Files

- `models/schedule.py`
- `services/scheduler_service.py`
- `data/scheduled_payments.json`
- `docs/transaction_schema.md`
- `docs/merchant_schema.md`
