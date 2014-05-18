# -*- coding: utf-8 -*-
from django.forms import ModelForm
from models import Event, Event_Part


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'city', 'date', 'desc')


class EventPartForm(ModelForm):
    class Meta:
        model = Event_Part
        fields = ('event', 'partner', 'status')