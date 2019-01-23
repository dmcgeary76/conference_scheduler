from django.db import models

# Create your models here.
class Session_Model(models.Model):
    presenter       = models.CharField(max_length=120)
    org             = models.CharField(max_length=120)
    email           = models.CharField(max_length=120)
    title           = models.CharField(max_length=120)
    description     = models.CharField(max_length=1500)
    domain          = models.CharField(max_length=120)
    age_range       = models.CharField(max_length=120)
    code            = models.CharField(max_length=120)
    room            = models.CharField(max_length=120)
    time_slot       = models.CharField(max_length=120)
    room_limit      = models.PositiveIntegerField()
    seats           = models.PositiveIntegerField()


class Choice_Model(models.Model):
    time_slot       = models.CharField(max_length=10)
    user_id         = models.PositiveIntegerField()
    session_id      = models.PositiveIntegerField()
