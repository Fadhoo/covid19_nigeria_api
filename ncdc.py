import os

import django
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import ncdc_api.settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'ncdc_api.settings'
django.setup()

from ncdc_data.models import CovidData

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


def get_ncdc_data():
    # CovidData.objects.all().delete()
    date = datetime.now()
    samples_tested = soup.find('div', class_='card newcol order-card').span.text
    i = 0
    cards = [{"date": date}, {"title": "samples_tested", "value": samples_tested}]

    for card in soup.find_all('div', class_='col-xs-3 col-md-3 col-xl-3'):
        title = card.find('h6', class_='text-white').text
        card[i] = card.find('span').text
        cards.append({"title": title, "value": card[i]})
        i += i

    print(cards)

    # saving data to the db
    model_instances = [CovidData(date=(cards[0]['date']),
                                 samples_tested=(cards[1]['value']),
                                 confirmed_cases=cards[2]['value'],
                                 active_cases=cards[3]['value'],
                                 discharged_cases=cards[4]['value'],
                                 deaths=cards[5]['value'], )]
    CovidData.objects.bulk_create(model_instances)


get_ncdc_data()

