# -*- coding : utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from personal_calendar.views import profile
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout, {'next_page':'/accounts/login/'}),
    url(r'^accounts/profile/$', profile),

)
