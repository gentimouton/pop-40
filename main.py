from google.appengine.ext.db import Model
from views import MainPage, Pop40Page
import logging
import os
import webapp2 as webapp

logging.getLogger().setLevel(logging.DEBUG)
logging.info('App was loaded.')

# check if the DB is storing all the available weeks
for filename in os.listdir('data'):
    datestr = filename.split('_', 1)[1].rstrip('.rss')
    week = Model.get_by_key_name(datestr) # TODO: this is not working
    if not week:
        logging.info(datestr + ' was missing')

app = webapp.WSGIApplication([('/', MainPage),
                              ('/all', Pop40Page)],
                              debug=True)
