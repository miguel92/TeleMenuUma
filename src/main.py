from views import ShowAds, NewAd, DeleteAd, EditAd,SearchRes, Welcome
from viewsAdmin import Admin
# Escribir todas las paginas que vamos a crear.
# Arrancar en local: python "C:\Users\migue\AppData\Local\Google\Cloud SDK\google-cloud-sdk\platform\google_appengine\dev_appserver.py" .
import webapp2

app = webapp2.WSGIApplication([
        ('/', Welcome), 
        ('/new', NewAd), 
        ('/edit/([\d]+)', EditAd),
        ('/delete/([\d]+)', DeleteAd),
        ('/search', SearchRes),
        ('/search', SearchRes),
        ('/admin',Admin)  
        ],
        debug=True)
