# -*- coding : utf-8 -*-
from django.test import TestCase
from models import Event_Part, Event
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class TestEvent_Part(TestCase):
    def test_create_user(self):
        """
        We need a user to invite to an event. We'll create one.
        """
        partner1 = User(first_name="John", last_name="Doe")
        partner1.save()
        # Now let check if the item is saved.
        partner = User.objects.get(first_name="John")
        self.assertEqual(partner.last_name, "Doe")

    def test_create_event(self):
        event = Event(
        name= 'A new event', desc=""" This new event is created to show how works test units.""",
        date= datetime.now(),
        city= "Somewhere"
                     )
        event.save()
        event = Event.objects.get(nom="A new Event")
        self.assertEqual(event.city, u'Somewhere')

    def test_create_event_partners(self):
        self.test_create_user()
        self.test_create_event()
        partner = User.objects.get(first_name="John")
        event = Event.objects.get(name='A new event')
        evnt_part = Event_Part(event=event, partner=partner, status=1)
        evnt_part.save()
        evnt = Event_Part.objects.get(event=event, partner=partner)
        self.assertEqual(evnt.status, 1)
