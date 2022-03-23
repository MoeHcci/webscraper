
import requests #https://docs.python-requests.org/en/latest/
import bs4 #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import lxml
import html5lib
import pandas as pd
import time


def check():  # Method 2

    # 1. Using the requests library and its get method to connect to the web page

    response = requests.get(f'https://www.autoparkmississauga.ca/used/group/pg/2')
    soup = BeautifulSoup(response.text, 'lxml')

    results_prices = soup.find_all('span', class_='vehicle-price-2-new suggestedPrice-price')
    results_city = soup.select(
        'td > var')  # This method means any element named var directly within a td element and nothing in between

    print(results_prices)
    print(results_city)


def check999():  # Method 2

    # 1. Using the requests library and its get method to connect to the web page

    response = requests.get(f'https://www.autoparkmississauga.ca/used/group/pg/83')
    soup = BeautifulSoup(response.text, 'lxml')
    results_city = soup.select('td > var')

    print(results_city)
    print(len(results_city))

    if results_city == []:
        print('hi')


if __name__ == '__main__':
    check()
    check999()
