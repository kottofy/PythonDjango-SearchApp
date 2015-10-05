#@author: Kristin Ottofy
"""
Definition of urls for SearchApp.
"""

from django.conf.urls import patterns, url
from app.views import query

urlpatterns = patterns('',
    url(r'^$', query),
    url(r'^query$', query)
)
