#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : letsagree/urls.py
#
#       Creation Date : Wed 06 Feb 2019 07:49:20 PM EET (19:49)
#
#       Last Modified : Wed 19 Aug 2020 10:15:47 PM EEST (22:15)
#
# ==============================================================================

from django.urls import path
from letsagree.views import PendingView

app_name = "letsagree"

urlpatterns = [path("", PendingView.as_view(), name="pending")]
