from bs4 import BeautifulSoup as bs
from .models import Session_Model
import requests

# set the target url for processing
url = 'fr1.html'
srt = [[]]
lrt = [[]]
selrt = [[]]
icrt = [[]]

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
    if item[6] == 'SCIENCE ROUND TABLE':
        item[10] = time_slot
        srt.append(item)
    elif item[6] == 'LITERACY ROUND TABLE':
        item[10] = time_slot
        lrt.append(item)
    elif item[6] == 'SEL ROUND TABLE':
        item[10] == time_slot
        selrt.append(item)
    elif item[6] == 'INTEGRATED CURRICULUM ROUND TABLE':
        item[10] == time_slot
        print('ICRT Found')
        icrt.append(item)
    else:
        try:
            room_limit = int(item[11])
        except:
            room_limit = 1000
        submission = Session_Model(
            presenter   = item[0],
            org         = item[1],
            email       = item[2].lower(),
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


def meta_session1(sessions):
    meta_desc = ''
    for session in sessions:
        try:
            meta_desc = meta_desc + session[0] + ' - ' +  session[1] + '<br /><br />' + session[4] + '<br /><br />'
        except:
            pass
    submission = Session_Model(
        presenter       = 'Various',
        org             = 'Various',
        email           = 'Various',
        title           = sessions[1][6],
        description     = meta_desc,
        domain          = sessions[1][6],
        age_range       = sessions[1][7],
        code            = sessions[1][8],
        room            = sessions[1][9],
        time_slot       = '2:00',
        room_limit      = 30,
        seats           = 0
    )
    submission.save()
    submission = Session_Model(
        presenter       = 'Various',
        org             = 'Various',
        email           = 'Various',
        title           = sessions[1][6],
        description     = meta_desc,
        domain          = sessions[1][6],
        age_range       = sessions[1][7],
        code            = sessions[1][8],
        room            = sessions[1][9],
        time_slot       = '12:45',
        room_limit      = 30,
        seats           = 0
    )
    submission.save()


def meta_session2(sessions):
    meta_desc = ''
    for session in sessions:
        try:
            meta_desc = meta_desc + session[0] + ' - ' +  session[1] + '<br /><br />' + session[4] + '<br /><br />'
        except:
            pass
    submission = Session_Model(
        presenter       = 'Various',
        org             = 'Various',
        email           = 'Various',
        title           = sessions[1][6],
        description     = meta_desc,
        domain          = sessions[1][6],
        age_range       = sessions[1][7],
        code            = sessions[1][8],
        room            = sessions[1][9],
        time_slot       = '10:15',
        room_limit      = 30,
        seats           = 0
    )
    submission.save()
    submission = Session_Model(
        presenter       = 'Various',
        org             = 'Various',
        email           = 'Various',
        title           = sessions[1][6],
        description     = meta_desc,
        domain          = sessions[1][6],
        age_range       = sessions[1][7],
        code            = sessions[1][8],
        room            = sessions[1][9],
        time_slot       = '11:30',
        room_limit      = 30,
        seats           = 0
    )
    submission.save()


def main():
    get_data(url)
    meta_session1(srt)
    meta_session1(selrt)
    meta_session2(lrt)
    meta_session2(icrt)
    print(srt)
