# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from views import create_account

urlpatterns = patterns('',
    # Login urls :
    url(r'^login/$', login, {'template_name':'usermanagement/login.html'}),
    url(r'^logout/$', logout, {'next_page':'/user/login'}),

    # Account management urls :
    url(r'^create_account/$', create_account),
    url(r'^succes/$', TemplateView.as_view(template_name="usermanagement/succes.html")),
    url(r'^profile/$', login_required(TemplateView.as_view(template_name="usermanagement/profile.html"))),
)
