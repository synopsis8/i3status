#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def get_exchange_rate():
    url = "https://www.boursorama.com/bourse/devises/taux-de-change-euro-dirham-EUR-AED/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    exchange_rate = soup.select_one("#main-content > div > section > header > div > div > div.c-faceplate__company > div.c-faceplate__info > div > div.c-faceplate__price.c-faceplate__price--inline > span.c-instrument.c-instrument--last").text
    return exchange_rate

def get_percentage_info():
    url = "https://www.boursorama.com/bourse/devises/taux-de-change-euro-dirham-EUR-AED/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    percentage_info = soup.select_one("#main-content > div > section > header > div > div > div.c-faceplate__company > div.c-faceplate__info > div > div.c-faceplate__fluctuation.c-faceplate__fluctuation--inline > span > span").text
    return percentage_info

def myround(val, r=4):
    return "{:.{}f}".format(float(val), r).rstrip('0').rstrip('.') if '.' in str(val) else str(val)

if __name__ == "__main__":
    exchange_rate = get_exchange_rate()
    percentage_info = get_percentage_info()
    print("€ 1 = {} AED {}".format(myround(exchange_rate), percentage_info))

