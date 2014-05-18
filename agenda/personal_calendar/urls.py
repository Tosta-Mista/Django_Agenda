# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns, include
from views import create, details

urlpatterns = patterns('',
    url(r'^create/$', create),
    url(r'^(\+d)/details/$', details),
)