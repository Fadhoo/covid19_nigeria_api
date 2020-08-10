from bs4 import BeautifulSoup
import requests
from datetime import datetime

source = requests.get('https://covid19.ncdc.gov.ng/').text

soup = BeautifulSoup(source, 'html5lib')


# print(soup.prettify())

# for name in soup.find('thead').tr:
#     table_head = name
#     print(table_head)

# for rows in soup.find_all('tr'):
#     for row in rows:
#         for state in row:
#             print(state)


def total_samples_tested():
    date = datetime.now()
    samples_tested = soup.find('div', class_='card newcol order-card').span.text
    print('Total samples tested:' + samples_tested, date)

    i = 0
    cards = []

    for cards in soup.find_all('div', class_='col-xs-3 col-md-3 col-xl-3'):
        title = cards.find('h6', class_='text-white').text
        cards[i] = cards.find('span').text
        i += i
        print(title, cards[i])


total_samples_tested()
