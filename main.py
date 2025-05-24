from models.merchant import Merchant
from services.merchant_service import save_merchant, merchant_exists


print("+","-"*17,"+")
print("| Welcome ClearFund |")
print("+","-"*17,"+")

while True:
    print("+","-"*25,"+")
    print("| Choose an option: ", " "*6, "|")
    print("| 1 - Register new merchant |")
    print("| 2 - List merchants", " "*6, "|")
    print("| 0 - Exit ", " "*15, "|")
    print("+","-"*25,"+")

    choice = input("Enter your choice 1, 2 or 0: ").strip()

    if choice == "0":
        print("+","-"*45,"+")
        print("| Thank you for using the ClearFund. Goodbye! |")
        break

    elif choice == "1":
        id_CF = int(input("enter with your ID with : "))

        if merchant_exists(id_CF):
            print("Merchant with ID {} already exists! Registration canceled. ".format(id_CF))
            continue

        company_name = str(input("Enter with your company name: ")).strip().title()
        company_number = int(input("Enter with your company_number: "))
        vat_number = str(input("Enter with your vat number: ")).strip().title()
        tax_number = float(input("Enter with your tax number: "))
        bank_info = str(input("Enter with your bank account: ")).strip().title()

        merchant_obj = Merchant(id_CF,company_name, company_number,vat_number, tax_number,bank_info)
        save_merchant(merchant_obj)
        print("\nMerchant registered successfully!\n")

    elif choice =="2":
        print("+","-"*51,"+")
        print("| Sorry, but the function hasn't been implemented yet |")
        print("+","-"*51,"+")
        break

    else:
        print("+","-"*67,"+")
        print("| Invalid option! Please choose one of the option listed in the menu. |")
        print("+","-"*67,"+\n")

