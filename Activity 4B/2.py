import csv

def load_exchange_rates(file_path):
    exchange_rates = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            exchange_rates[row[0]] = float(row[2])
    return exchange_rates

def convert_currency(amount, currency_code, exchange_rates):
    if currency_code in exchange_rates:
        return amount * exchange_rates[currency_code]
    else:
        return None

def main():
    file_path = "Activity 4B/currency.csv" 
    exchange_rates = load_exchange_rates(file_path)
    
    try:
        usd_amount = float(input("How much dollar do you have? "))
        currency_code = input("What currency you want to have? ").upper()
        
        converted_amount = convert_currency(usd_amount, currency_code, exchange_rates)
        
        if converted_amount is not None:
            print(f"\nDollar: {usd_amount} USD")
            print(f"{currency_code}: {converted_amount:.2f}")
        else:
            print("Sorry, currency code not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for dollars.")
        
main()