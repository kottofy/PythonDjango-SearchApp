#@author: Kristin Ottofy

from django.conf import settings
import tweepy
import requests
import json
from urllib.request import urlopen

def get_twitter_api(twitter_settings):
    
    api = []

    try:
        consumer_key = twitter_settings['consumer_key']
        consumer_secret = twitter_settings['consumer_secret']
        access_token = twitter_settings['access_token']
        access_token_secret = twitter_settings['access_token_secret']

        # Create auth token
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
    
        # Get API Handler
        api = tweepy.API(auth)
    except:
        print("Error getting Twitter API")
        pass
    return api

def auth_twitter():

    twitter_settings = []

    try:
        twitter_settings = settings.PROVIDER_CREDENTIALS['TWITTER']
       
    except:
        print("Unable to authenticate twitter")
        pass

    return twitter_settings

def search_twitter(word):

    twitter_results = []

    try:
        twitter_settings = auth_twitter()
        api = get_twitter_api(twitter_settings)
        twitter_results = api.search(q=word, count=25, result_type="recent")
    except:
        print("Something went wrong getting Twitter results")
        pass

    return twitter_results

#try to get ip address from request
def  get_ip_address(request):
    ip = ''
    try:
        ip = request.META['REMOTE_ADDR']
        print("ip: " + ip)
    except: 
        print("problem getting ip")
        pass
    return ip

# try to make url to later get json object with location info
def make_url(ip):
    url = ''
    try:
        url = 'http://freegeoip.net/json/'+ip
        print("url: " + url)
    except:
        print("problem making url")
        pass
    return url;

# get user latitude and longitude ready for twitter search
def get_location(url):
    location = ''
    try:
        r = requests.get(url)
        print("got r")
        json_obj = json.loads(r.text)
        print("got json_obj")
        latitude = str(json_obj['latitude'])
        longitude = str(json_obj['longitude'])
        location = latitude+","+longitude+",100mi"
    except:
        print("problem getting location")
        pass
    return location

# Problem! This method does not work on Azure!
def search_twitter_by_location(request, word):

    twitter_results = []

    try:
        #ip = settings.TEST_CREDENTIALS['TEST_IP']['ip']
        ip = get_ip_address(request)
        url = make_url(ip)
        location = get_location(url)

        twitter_settings = auth_twitter()
        api = get_twitter_api(twitter_settings)
        twitter_results = api.search(q=word, count=25, result_type="recent", geocode=location)
    except:
        print("Something went wrong getting Twitter results by location")
        pass

    return twitter_results

# TODO require authentication once to speed up performance