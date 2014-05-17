# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns, include
from views import create

urlpatterns = patterns('',
    url(r'^create/$', create),
)