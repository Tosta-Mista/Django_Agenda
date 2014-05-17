# -*- coding : utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin urls :
    url(r'^admin/', include(admin.site.urls)),

    # Usermanagement urls :
    url(r'^user/', include('usermanagement.urls')),

)
