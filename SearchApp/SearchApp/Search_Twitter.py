﻿#@author: Kristin Ottofy

from django.conf import settings
import tweepy
import requests
import json

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

def search_twitter_by_location(word):
    print("location on!")
    twitter_results = []

    try:
        url = 'http://freegeoip.net/json/'
        try:
            r = requests.get(url)
            print("got r")
            json_obj = json.loads(r.text)
            print("got json_obj")
            latitude = str(json_obj['latitude'])
            longitude = str(json_obj['longitude'])
        except Exception as e:
            print(e.with_traceback)
            print("Location could not be determined automatically")

        twitter_settings = auth_twitter()
        api = get_twitter_api(twitter_settings)
        twitter_results = api.search(q=word, count=25, result_type="recent", geocode=latitude+","+longitude+",100mi")
    except:
        print("Something went wrong getting Twitter results by location")
        pass

    return twitter_results

# TODO add search twitter by location functionality
    #( geocode – Returns tweets by users located within a given radius of the given latitude/longitude. 
    # The location is preferentially taking from the Geotagging API, but will fall back to their Twitter 
    # profile. The parameter value is specified by “latitide,longitude,radius”, where radius units must 
    # be specified as either “mi” (miles) or “km” (kilometers). Note that you cannot use the near operator 
    # via the API to geocode arbitrary locations; however you can use this geocode parameter to search 
    # near geocodes directly.)
# TODO require authentication once to speed up performance