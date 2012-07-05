from google.appengine.ext import db
from models import week_key, Song
import jinja2
import json
import logging
import os
import rssloader
import webapp2 as webapp


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render())



class Pop40Page(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write(json.dumps(rssloader.rssdata))
        
        week_date = '2012-06-16'
                
        # add a song to the db
        song = Song(parent=week_key(week_date))
        song.artist = 'Eminem'
        song.title = 'Slim Shady'
        song.rank = 5
        song.put()

        # read
        songs = Song.gql("WHERE ANCESTOR IS :1 "
                         "ORDER BY rank DESC LIMIT 10",
                         week_key(week_date))
        res = {}
        week = []
        for song in songs:
            sg = {'artist':song.artist,
                  'rank':song.rank,
                  'title':song.title}
            week.append(sg)
        res[week_date] = week
        
        self.response.out.write(json.dumps(res))
        
