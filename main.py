from models.merchant import Merchant
from models.transaction import Transaction
from services.merchant_service import save_merchant, merchant_exists, generate_id
from services.transaction_service import save_transaction, process_transaction, generate_id_stan

print("+","-"*17,"+")
print("| Welcome ClearFund |")
print("+","-"*17,"+")

while True:
    print("+","-"*30,"+")
    print("| Choose an option: ", " "*11, "|")
    print("| 1 - Register new merchant", " "*4, "|")
    print("| 2 - List merchants", " "*11, "|")
    print("| 3 - Register new transaction", " ", "|")
    print("| 0 - Exit ", " "*20, "|")
    print("+","-"*30,"+")

    choice = input("Enter your choice 1, 2 or 0: ").strip()

    if choice == "0":
        print("+","-"*43,"+")
        print("| Thank you for using the ClearFund. Goodbye! |")
        print("+","-"*43,"+")
        break
# Data entry for merchant registration
    elif choice == "1":
        id_CF = generate_id()


        # id_CF = int(input("enter with your ID with : "))
        #
        # if merchant_exists(id_CF):
        #     print("Merchant with ID {} already exists! Registration canceled. ".format(id_CF))
        #     continue

        company_name = input("Enter the company name (e.g., ClearFunds Ltd.): ").strip().title()
        company_number = int(input("Enter the company registration number (numeric only – e.g., 123456789): "))
        if merchant_exists(company_number):
            print("\nMerchant with Company number {} already exists! Registration cancelad. \n".format(company_number))
            continue
        vat_number = input("Enter the VAT number (e.g., IE123456789A): ").strip().upper()
        # fee_rate = float(input("Enter the transaction fee percentage as a decimal (e.g., 0.025 for 2.5%): "))
        debit_fee = float(input("Enter the percentage of the debit transaction fee (e.g., 0.025 for 2.5%) "))
        credit_fee = float(input("Enter the percentage of the credit transaction fee (e.g., 0.025 for 2.5%) "))
        bank_info = input("Enter the bank account details (e.g., BankName 1234-5 / Agency 0001): ").strip()


        merchant_obj = Merchant(id_CF,company_name, company_number,vat_number,debit_fee, credit_fee,bank_info)
        save_merchant(merchant_obj)
        print("\nMerchant registered successfully!\n")

    elif choice =="2":
        print("+","-"*51,"+")
        print("| Sorry, but the function hasn't been implemented yet |")
        print("+","-"*51,"+")
        break

# Data entry to register transactions
    elif choice =="3":
        mti = int(input("Enter the MTI (Message Type Indicator) – e.g., 0200 for transaction request: "))
        transaction_type = input("Enter with type of operation (e.g debit or credit): ")
        merchant_id = input("Enter the Merchant ID (must match an existing registered merchant): ")
        company_number = input("Enter the Company Number (corporate identifier of the merchant): ")
        mcc = input("Enter the Merchant Category Code (MCC – e.g., 5411 for grocery store): ")
        fee_rate = ""
        terminal_id = input("Enter the Terminal ID (e.g., POS/TEF terminal ID): ")
        transaction_datetime = input("Enter the transaction date and time (format: DD-MM-YYYY HH:MM:SS): ")
        # stan = int(input("Enter the STAN (System Trace Audit Number – unique sequential ID): "))
        stan = generate_id_stan()
        nsu = input("Enter the NSU (Unique Sequential Number provided by the acquirer/processor): ")
        auth_code = input("Enter the Authorization Code (from acquirer or processor): ")
        currency_code = input("Enter the Currency Code (e.g., 986 for BRL): ")
        total_amount = float(input("Enter the Total Transaction Amount (e.g., 150.00): "))
        instalment_count = int(input("Enter the Number of Instalments (1 if no instalments): "))
        instalment_amount = float(input("Enter the Instalment Value (total value / number of instalments): "))
        original_data = input("If this is a reversal or related transaction, enter the Original STAN (optional): ")


        transaction_obj = Transaction(mti,transaction_type,  merchant_id, company_number, mcc,fee_rate, terminal_id, transaction_datetime,
                                      stan, nsu, auth_code, currency_code, total_amount, instalment_count,
                                      instalment_amount, original_data)
        process_transaction(transaction_obj)

        print("\nTransaction registered successfully!\n")

    else:
        print("+","-"*67,"+")
        print("| Invalid option! Please choose one of the option listed in the menu. |")
        print("+","-"*67,"+\n")

