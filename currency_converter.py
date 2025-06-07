import requests

CURRENCIES = ['RUB', 'EUR', 'USD', 'KZT']


def convert(amount, from_currency, to_currency):
    if from_currency not in CURRENCIES:
        raise ValueError(f"Unsupported currency: {from_currency}")
    if to_currency not in CURRENCIES:
        raise ValueError(f"Unsupported currency: {to_currency}")
    url = (
        f"https://api.exchangerate.host/convert"
        f"?from={from_currency}&to={to_currency}&amount={amount}"
    )
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    return data.get('result')


if __name__ == '__main__':
    print("Available currencies:", ', '.join(CURRENCIES))
    amount = float(input("Amount: "))
    from_currency = input("From currency: ").upper()
    to_currency = input("To currency: ").upper()
    try:
        result = convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except Exception as e:
        print("Error:", e)
