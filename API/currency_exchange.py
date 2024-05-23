import requests


class Currency:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

    def exchange(self, from_currency, to_currency, amount):
        response_link = self.base_url + from_currency
        response = requests.get(response_link)
        data = response.json()
        if data["result"] == "error":
            print(f'Помилка: {data["error-type"]}')
            return
        else:
            my_sum = data["conversion_rates"][to_currency] * amount
            print(f"{amount} {from_currency} = {my_sum:.2f} {to_currency}")


def main():
    api_key = 'd6612d7e4f80ceaf445b60eb'  # Replace with your actual API key
    converter = Currency(api_key)

    from_currency = input("Enter the currency code you want to convert from: ").upper()
    to_currency = input("Enter the currency code you want to convert to: ").upper()
    amount = float(input("Enter the amount you want to convert: "))

    converter.exchange(from_currency, to_currency, amount)


if __name__ == "__main__":
    main()
