# Demo
http://kristinottofysearchapp.azurewebsites.net

# About
This is a [Python](https://www.python.org/)/[Django](https://www.djangoproject.com/) application.
This application takes input as a query and returns search results from [Wikipedia](https://www.wikipedia.org/) 
and [Twitter](https://twitter.com/). 

# Getting Twitter Results
The Twitter search is completed through [Tweepy](http://tweepy.readthedocs.org/en/v3.4.0/). This applications is
currently set to use Twitter's REST API which returns a limited amount of results (within a week or so) and does not stream
live data. It is set to deliver the most recent results. This application has also capped the amount of results to return from the search.

# Getting Wikipedia Results
The Wikipedia search is completed through [Python's Wikipedia Package](https://pypi.python.org/pypi/wikipedia/).
Often, queries cause Disambiguation Errors. Currently, those are handled on a limited basis. Ex. if a query like 'banana'
returns a DisambiguationError, the error is parsed and the available pages in the error are added to the results. Therefore,
this error can happen again on one of those pages, but this application will only add so many results.

# Performance Positives
1. Handles no results receieved from either Twitter or Wikipedia by displaying message.
2. If one API is down, the other will still work.
3. Site is responsive and mobile friendly with a Bootstrap collapsable menu.
4. Simple Django setup with templates, forms, views, etc. allows for pretty easy to read code.
5. Twitter Authentication details are not uploaded to GitHub.
6. Uses HTML5 to require an input.

# Performance Negatives (TODOs)
1. Asks for twitter authorization at every search. Twitter search is fast but display of results is slow for Twitter and Wikipedia results.
2. layout.html is HTML5 validated. search.html is mostly HTML5 validated except for the href attribute on a element contains "illegal characters".
3. PageSpeed: Server response time is 8.4 seconds - needs to speed up!!

# PageSpeed Analyzation
http://kristinottofysearchapp.azurewebsites.net/?query=kristinottofy
as of 10/5/15 11:54 am EST
## Mobile: 66/100
### Should fix:
- Eliminate render-blocking JavaScript and CSS in above-the-fold content
- Reduce server response time

### Consider fixing:
- Leverage browser caching
- Optimize images
- Minify JavaScript
- Minify CSS

### Passed Rules:
- Avoid landing page redirects
- Enable compression
- Minify HTML
- Prioritize visible content

### User Experience:

#### Consider Fixing:
- Size tap targets appropriately

#### Passed Rules:
- Avoid app install interstitials that hide contentBETA
- Avoid plugins
- Configure the viewport
- Size content to viewport
- Use legible font sizes

## Desktop: 54/100

### Should fix:
- Reduce server response time

### Consider fixing:
- Eliminate render-blocking JavaScript and CSS in above-the-fold content
- Leverage browser caching
- Optimize images
- Minify JavaScript
- Minify CSS

### Passed Rules:
- Avoid landing page redirects
- Enable compression
- Minify HTML
- Prioritize visible content

# TODO
1. Move Search bar and Submit button to nav-bar. Explore possibility of new home page with search in the middle.
2. Create option to search twitter by user location. See if it's possible to request IP address, use API to search for IP latitude and longitude, use Tweepy GeoCode.
3. Redirect to pretty error page when issues are encountered.
4. Create alert system so admin can know real-time errors.
5. Have search.html HTML5 validated.
6. Figure out how to make Twitter results all the same for a particular query.
7. Create DisambiguationError handling function for code readability. 
8. (Optional-speed up server response preferred!) Display "Working on it..." type of message when query is being processed.