from views import ShowAds, NewAd, DeleteAd, EditAd
# Escribir todas las paginas que vamos a crear.
import webapp2

app = webapp2.WSGIApplication([
        ('/', ShowAds), 
        ('/new', NewAd), 
        ('/edit/([\d]+)', EditAd),
        ('/delete/([\d]+)', DeleteAd),
        ],
        debug=True)
