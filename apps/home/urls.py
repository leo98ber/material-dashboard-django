# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    # Add report
    path('add_subscription/', views.SubscriptionView.as_view(), name='add_subscription'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
