# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from forms import EventForm, EventPartForm
from models import Event, Event_Part


def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return HttpResponseRedirect('/agenda/%i/details/' % event.pk)
    else:
        form = EventForm()
    return render(request, 'personal_calendar/event/create.html', {'form': form})


def details(request, id):
    event = event.objects.get(pk = id)
    if request.method == "POST":
        form = EventPartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/agenda/%s/details/' % id)
    else:
        form = EventPartForm(initial= {'events': event})
        paticipants = [user.pk for user in event.partners.all()]
        form.fields['partners'].queryset=User.objects.exclude(pk__in = partners)
    return render(request, 'personal_calendar/event/details.html', {
        'event':event,
        'form':form
    })