# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns, include
from views import create, details
from django.views.generic.list import ListView
from models import Event

urlpatterns = patterns('',
    url(r'^lists/$', ListView.as_view(model= Event)),
    url(r'^create/$', create),
    url(r'^(\+d)/details/$', details),
)