# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.TodayView.as_view(),
        name='today'
    ),
    url(
        regex=r'^success',
        view=views.TodaySuccessView.as_view(),
        name='today_success'
    ),
]
