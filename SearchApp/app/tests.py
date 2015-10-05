"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from SearchApp.Search_Twitter import auth_twitter, get_twitter_api
from SearchApp.Search_Wikipedia import search_wikipedia
import wikipedia

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_search(self):
        """Tests the search page."""
        response = self.client.get('/query')
        self.assertContains(response, status_code = 200)

class TwitterTest(TestCase):
    def test_twitter_api_auth(self):
        """Tests to ensure getting twitter api assigns correct auth data"""
        PROVIDER_CREDENTIALS = {}
        PROVIDER_CREDENTIALS['TWITTER'] = {}
        PROVIDER_CREDENTIALS['TWITTER']['consumer_key'] = '111'
        PROVIDER_CREDENTIALS['TWITTER']['consumer_secret'] = '222'
        PROVIDER_CREDENTIALS['TWITTER']['access_token'] = '333'
        PROVIDER_CREDENTIALS['TWITTER']['access_token_secret'] = '444'
        twitter_settings = PROVIDER_CREDENTIALS['TWITTER']
        api = get_twitter_api(twitter_settings)

        self.assertEqual(api.auth.consumer_key, b'111')
        self.assertEqual(api.auth.consumer_secret, b'222')
        self.assertEqual(api.auth.access_token, '333')
        self.assertEqual(api.auth.access_token_secret, '444')

    def test_twitter_not_None_auth(self):
        """Tests to ensure getting twitter authentication settings is returning information"""
        twitter_settings = auth_twitter()
        self.assertIsNotNone(twitter_settings)

class WikipediaTest(TestCase):
    def test_wikipedia_results_is_none(self):
        """Tests no results are returned from Wikipedia"""
        wiki_results = search_wikipedia('kristinottofy');
        self.assertEquals(wiki_results, [])

    def test_wikipedia_raises_disambiguation_error(self):
        """Tests results are returned from Wikipedia"""
        self.assertRaises(wikipedia.DisambiguationError, wiki_results=search_wikipedia('banana'))