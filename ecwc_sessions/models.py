from django.db import models


# Create your models here.
class Session_Model(models.Model):
    presenter       = models.CharField(max_length=120)
    p_bio           = models.CharField(max_length=2500, blank=True)
    coop            = models.CharField(max_length=120, blank=True)
    org             = models.CharField(max_length=120, blank=True)
    title           = models.CharField(max_length=120)
    description     = models.CharField(max_length=2500)
    domain          = models.CharField(max_length=120, blank=True)
    age_range       = models.CharField(max_length=120, blank=True)
    comp            = models.CharField(max_length=120, blank=True)
    room            = models.CharField(max_length=120)
    time_slot       = models.CharField(max_length=120)
    duration        = models.CharField(max_length=120)
    room_limit      = models.PositiveIntegerField()
    seats           = models.PositiveIntegerField()


class gSession_Model(models.Model):
    presenter       = models.CharField(max_length=120)
    p_bio           = models.CharField(max_length=2500)
    coop            = models.CharField(max_length=120)
    org             = models.CharField(max_length=120)
    title           = models.CharField(max_length=120)
    description     = models.CharField(max_length=2500)
    domain          = models.CharField(max_length=120)
    age_range       = models.CharField(max_length=120)
    comp            = models.CharField(max_length=120)
    room            = models.CharField(max_length=120)
    time_slot       = models.CharField(max_length=120)
    duration        = models.CharField(max_length=120)
    room_limit      = models.PositiveIntegerField()
    seats           = models.PositiveIntegerField()


class Choice_Model(models.Model):
    time_slot       = models.CharField(max_length=10)
    user_id         = models.PositiveIntegerField()
    session_id      = models.PositiveIntegerField()


class gChoice_Model(models.Model):
    time_slot       = models.CharField(max_length=10)
    user_id         = models.PositiveIntegerField()
    session_id      = models.PositiveIntegerField()
