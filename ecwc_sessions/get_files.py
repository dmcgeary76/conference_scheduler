from bs4 import BeautifulSoup as bs
from .models import Session_Model
import requests

# set the target url for processing
url = 'fr1.html'


def get_data(url):
    link = open(url)
    soup = bs(link.read(), 'html.parser')
    master = []
    new_data = soup.find('tbody')
    for tr in new_data.find_all('tr'):
        values = [td.text for td in tr.find_all('td')]
        master.append(values)
    print(master[3])
    for item in master:
        if item[0] != '':
            if '&' in item[10]:
                time_slots = item[10].split(' & ')
                for time_slot in time_slots:
                    submit_session(item, time_slot)
            else:
                submit_session(item, item[10])


def submit_session(item, time_slot):
    try:
        room_limit = int(item[11])
    except:
        room_limit = 1000
    submission = Session_Model(
        presenter   = item[0],
        org         = item[1],
        email       = item[2],
        title       = item[4],
        description = item[5],
        domain      = item[6],
        age_range   = item[7],
        code        = item[8],
        room        = item[9],
        time_slot   = time_slot,
        room_limit  = room_limit,
        seats       = 0
    )
    submission.save()


def main():
    get_data(url)
