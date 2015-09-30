from django.conf.urls import patterns, include, url
from django.contrib import admin

import sms.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'individual_assignment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'sms.views.sms', name='sms'),
    url(r'^admin/', include(admin.site.urls)),
)
