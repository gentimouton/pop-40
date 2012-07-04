from views import MainPage, Pop40Page
import logging
import webapp2 as webapp
#from google.appengine.ext import webapp

logging.getLogger().setLevel(logging.DEBUG)
logging.info('App was loaded.')

app = webapp.WSGIApplication([('/', MainPage),
                              ('/pop40', Pop40Page)],
                              debug=True)
