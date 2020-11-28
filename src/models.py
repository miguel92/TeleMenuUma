from google.appengine.ext import ndb


class Ads(ndb.Model):

    author = ndb.StringProperty()
    text = ndb.StringProperty()
    priority = ndb.IntegerProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    
