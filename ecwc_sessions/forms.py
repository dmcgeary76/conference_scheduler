from django import forms
from .models import Session_Model, Choice_Model


class Session_Form(forms.ModelForm):
    presenter       = forms.CharField(max_length=120)
    p_bio           = forms.CharField(max_length=2500, required=False)
    coop            = forms.CharField(max_length=120, required=False)
    org             = forms.CharField(max_length=120, required=False)
    title           = forms.CharField(max_length=120)
    description     = forms.CharField(max_length=2500)
    domain          = forms.CharField(max_length=120, required=False)
    age_range       = forms.CharField(max_length=120, required=False)
    comp            = forms.CharField(max_length=120, required=False)
    room            = forms.CharField(max_length=120)
    time_slot       = forms.CharField(max_length=120)
    duration        = forms.CharField(max_length=120)
    room_limit      = forms.IntegerField()
    seats           = forms.IntegerField()
    class Meta:
        model = Session_Model
        fields = [
            'presenter',
            'p_bio',
            'coop',
            'org',
            'title',
            'description',
            'domain',
            'age_range',
            'room',
            'time_slot',
            'duration',
            'room_limit',
            'seats'
        ]


class Choice_Form(forms.ModelForm):
    time_slot       = forms.CharField(max_length=10)
    user_id         = forms.IntegerField()
    session_id      = forms.IntegerField()
    class Meta:
        model = Choice_Model
        fields = [
            'time_slot',
            'user_id',
            'session_id'
        ]


class Search_Form(forms.ModelForm):
    search_string   = forms.CharField(max_length=100)
    class Meta:
        fields = [
            'search_string'
        ]
