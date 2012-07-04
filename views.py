import rssloader
import json
import webapp2 as webapp

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('<a href="pop40">Pop 40</a>')


class Pop40Page(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(json.dumps(rssloader.rssdata))
