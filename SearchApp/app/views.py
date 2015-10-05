"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from SearchApp.Search_Twitter import search_twitter
from SearchApp.Search_Wikipedia import search_wikipedia

def query(request):
    try:                
        word = request.GET.get('query')                 # get the query phrase

        if word is not None:                            # if a query exists
            twitter_results = search_twitter(word)      # search Twitter and
                
            wiki_results = search_wikipedia(word)        # search Wikipedia
                
            context = {
                'word': word,
                'twitter_results': twitter_results,
                'wiki_results':   wiki_results
            }
        else:                                           # if a query does not exist
            context = {}                                # there is no context
    except:
        context = {}

    return render(request, 'app/search.html', context)

# TODO add error page redirection
# TODO Deploy to Heroku