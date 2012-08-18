from google.appengine.ext import db
from lib import dictify
from models import week_key, Song
import datetime
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


########################## JSON #########################

class Pop40Page(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write(json.dumps(rssloader.rssdata))
        
        week_date = '2012-06-16'

        # read
        songs = Song.gql("WHERE ANCESTOR IS :1 "
                         "ORDER BY rank DESC LIMIT 10",
                         week_key(week_date))
        res = {}
        res[week_date] = [db.to_dict(song) for song in songs]
        #res[week_date] = [dictify.to_dict(song) for song in songs]
        
        self.response.out.write(json.dumps(res, default=dthandler))
        

# provide handler for converting datetime objects to json
# from http://stackoverflow.com/a/2680060/856897
def dthandler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise (TypeError,
               'Object of type %s with value of %s is not JSON serializable' 
               % (type(obj), repr(obj)))
