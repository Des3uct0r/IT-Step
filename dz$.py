import requests


def get_rate(aud):
    aud_amount = float(input("Enter the amount of AUD: "))
    url = 'https://bank.gov.ua/ua/markets/exchangerates'
    r = requests.get(url)
    t = r.text.split("<td")
    rates = []
    for p in t:
        if 'data-label="Офіційний курс"' in p:
            rates.append(p.split(">")[1].split("<")[0])
    return f"UAH to AUD : {rates[0]} UAH per {aud_amount} AUD."




print(get_rate())