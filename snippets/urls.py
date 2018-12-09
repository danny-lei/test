#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url
import views
from rest_framework.urlpatterns import format_suffix_patterns


# urlpatterns = [
#     url('^$', views.snippet_list),
#     url('(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]



urlpatterns = [
    url('^$', views.SnippetList.as_view()),
    url('(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
