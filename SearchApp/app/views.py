"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, Template, Context
from datetime import datetime, timedelta
import tweepy
import wikipedia
import json
from app.forms import SearchForm
from SearchApp.Search_Twitter import search_twitter
from SearchApp.Search_Wikipedia import searchWikipedia

#def query(request):
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/search.html')
    

def query(request):
    try:
        word = request.GET.get('query')

        twitter_results = search_twitter(word)

        wiki_results = searchWikipedia(word)
    
        context = {
            'word': word,
            'twitter_results': twitter_results,
            'wiki_results':   wiki_results
        }
    except:
        context = {}

    return render(request, 'app/search.html', context)


#def home(request):
#    """Renders the home page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/index.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'Home Page',
#            'year':datetime.now().year,
#        })
#    )

#def contact(request):
#    """Renders the contact page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/contact.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'Contact',
#            'message':'Your contact page.',
#            'year':datetime.now().year,
#        })
#    )

#def about(request):
#    """Renders the about page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/about.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'About',
#            'message':'Your application description page.',
#            'year':datetime.now().year,
#        })
#    )
