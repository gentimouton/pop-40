from google.appengine.ext import db


class Song(db.Model):
    """ Models a weekly song entry. """
    artist = db.StringProperty()
    title = db.StringProperty()
    rank = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    

def week_key(week_date):
    """Constructs a Datastore key for a Week entity."""
    return db.Key.from_path('Week', week_date)
