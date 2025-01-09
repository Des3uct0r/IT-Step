import requests


def get_rate():
    aud_amount = float(input("Enter how many  you need: "))
    url = 'https://bank.gov.ua/ua/markets/exchangerates'
    rp = requests.get(url)
    t = rp.text.split("<td")
    rates = []
    for p in t:
        if 'data-label="Офіційний курс"' in p:
            rates.append(p.split(">")[1].split("<")[0].replace(',','.'))
    rate_of_aud = float(rates[0])
    res = aud_amount * rate_of_aud
    return f"{res} UAH for {aud_amount} AUD."



print(get_rate())