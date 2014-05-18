# -*- coding : utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

## Enum :
status_choice = (
    (0, "host"),
    (1, "visitor"),
    (2, "old")
)

##


class Event(models.Model):
    """
    This class include all info about an event.
    """
    name = models.CharField(max_length=250, unique=True)
    desc = models.TextField()
    partners = models.ManyToManyField(
        User,
        through="Event_Part",
        )
    date = models.DateTimeField()
    city = models.TextField()


class Event_Part(models.Model):
    event = models.ForeignKey(Event)
    partner = models.ForeignKey(User)
    status = models.IntegerField(choices=status_choice)
    class Meta:
        unique_together = ("event", "partner")