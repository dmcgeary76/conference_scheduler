from django.contrib.auth.models import User
import csv

sfile='users.csv'

def add_users():
    with open(sfile, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if 'Last Name' not in row[0]:
                username = row[1].lower() + '.' + row[0].lower()
                try:
                    test_user = User.objects.get(username=username)
                    print(username + ' already exists.')
                except:
                    user = User.objects.create_user(username, row[2], 'ecwc2019!')
                    user.last_name = row[0]
                    user.first_name = row[1]
                    user.save()
