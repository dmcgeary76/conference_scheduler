from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import csv

def enroll_them():
    dataReader = csv.reader(open('roll_call.csv'), delimiter=',', quotechar='"')
    for item in dataReader:
        try:
            user = get_object_or_404(User, username=item[2])
        except:
            user = User(
                last_name   = item[0],
                first_name  = item[1],
                username    = item[2],
                email       = item[2].lower(),
            )
            user.set_password('ecwc2019!')
            user.save()
