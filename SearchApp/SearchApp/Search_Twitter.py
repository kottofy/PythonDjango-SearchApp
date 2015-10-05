from django.conf import settings
import tweepy

def search_twitter(word):

    twitter_results = []

    try:
        twitter_settings = settings.PROVIDER_CREDENTIALS['TWITTER']
        consumer_key = twitter_settings['consumer_key']
        consumer_secret = twitter_settings['consumer_secret']
        access_token = twitter_settings['access_token']
        access_token_secret = twitter_settings['access_token_secret']
    except:
        print("Unable to authenticate twitter")

    # Create auth token
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    # Get API Handler
    api = tweepy.API(auth)
    
    twitter_results = api.search(q=word, count=25, result_type="recent")

    return twitter_results

# TODO add search twitter by location functionality
# TODO require authentication once to speed up performance