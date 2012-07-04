import os.path
from lib import feedparser

# Imports are cached by appengine.
# Hence rssdata will take a while to be computed when the module is loaded
# (ie at the first request).
# But for the following requests, rssdata will be cached.   
# See https://developers.google.com/appengine/docs/python/runtime#App_Caching

""" Parse all the RSS """
rssdata = {}
for filename in os.listdir('data'):
    datestr = filename.split('_', 1)[1].rstrip('.rss')
    rss = feedparser.parse(os.path.join('data', filename))
    songs = []
    for entry in rss.entries:
        song, artistrank = tuple(entry.description.split('by', 1))
        artist, rank = artistrank.split('ranks #', 1)
        songs.append({'song':song, 'artist':artist, 'rank':rank}) 
    rssdata[datestr] = songs

def getrssdata():
    return rssdata
