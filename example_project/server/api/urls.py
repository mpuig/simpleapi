# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from simpleapi import Route
from handlers import OldCalculator, NewCalculator, SomeFunctions

urlpatterns = patterns('',
	(r'^calculator/multiple/$', Route(OldCalculator, NewCalculator)),
	(r'^calculator/one/$', Route(OldCalculator)),
	(r'^functions/$', Route(SomeFunctions))
)