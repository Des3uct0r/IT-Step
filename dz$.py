import requests


def get_rate():
    url = 'https://bank.gov.ua/ua/markets/exchangerates'
    try:
        r = requests.get(url)
        t = r.text.split("<td")
        rates = []
        for p in t:
            if 'data-label="Офіційний курс"' in p:
                rates.append(p.split(">")[1].split("<")[0])
        if not rates:
            return "Error: Rate not found."
        return f"UAH to USD rate: {rates[0]} UAH per 1 USD."
    except Exception as e:
        return f"Error: {e}"


print(get_rate())