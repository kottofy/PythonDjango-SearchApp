"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
import tweepy
import wikipedia
import json
from app.forms import SearchForm
from SearchApp.Search_Twitter import search_twitter
from SearchApp.Search_Wikipedia import searchWikipedia

def query(request):
    try:
        word = request.GET.get('query')

        if word is not None:
            twitter_results = search_twitter(word)

            wiki_results = searchWikipedia(word)
    
            context = {
                'word': word,
                'twitter_results': twitter_results,
                'wiki_results':   wiki_results
            }
        else:
            context = {}
    except:
        context = {}

    return render(request, 'app/search.html', context)