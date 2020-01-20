from bs4 import BeautifulSoup as bs
from .models import Session_Model
import requests, csv

# set the target url for processing
url = 'fr1.html'
sfile = 'ecwc.csv'
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


def get_data2():
    with open(sfile, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            times = row[16].upper().replace(' ','').replace('A.M.',' A.M.').replace('P.M.',' P.M.')
            if 'A.M.' in times or 'P.M.' in times:
                pass
            else:
                times = times.replace('10:15','10:15 A.M.').replace('11:30','11:30 A.M.').replace('12:45','12:45 P.M.').replace('2:00','2:00 P.M.')
            if row[1] != '' and row[0] != 'Timestamp':
                if '&' in times:
                    for time_slot in times.split('&'):
                        submit_session(row, time_slot, '1 Hour')
                elif '-' in times:
                    submit_session(row, times.split('-')[0], '2 Hours')
                else:
                    submit_session(row, times, '1 Hour')



def submit_session(item, time_slot, time_span):
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
            room_limit = int(item[17])
        except:
            room_limit = 1000
        finally:
            submission = Session_Model(
                presenter   = item[1],
                p_bio       = item[2],
                coop        = item[4],
                org         = item[3],
                email       = item[17].lower(),
                title       = item[5],
                description = item[6],
                domain      = item[7],
                comp        = item[8],
                age_range   = item[9],
                code        = item[0],
                room        = item[15],
                time_slot   = time_slot,
                duration    = time_span,
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

'''
def main():
    get_data(url)
    meta_session1(srt)
    meta_session1(selrt)
    meta_session2(lrt)
    meta_session2(icrt)
    print(srt)
'''
