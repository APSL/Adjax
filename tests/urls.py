#!/usr/bin/env python
# encoding: utf-8
# ----------------------------------------------------------------------------

from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',
    (r'^demo/', include('basic.urls')),
    (r'^tutorial/', include('tutorial.urls')),
)

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
