# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from forms import EventForm
from models import Event


def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return HttpResponseRedirect('/agenda/%i/details/'% event.pk)
    else:
        form = EventForm()
    return render(request, 'personal_calendar/event/create.html', {'form':form})

def details(request, id):
    event = Event.objects.get(pk = id)
    return render(request, 'personal_calendar/event/details.html', {'event':event})