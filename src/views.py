from datetime import datetime
import os
import webapp2
import jinja2

from google.appengine.ext import ndb

from models import Ads 

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


class BaseHandler(webapp2.RequestHandler):

    def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))


class ShowAds(BaseHandler):
    
    def get(self):
        ads = Ads.query()
        self.render_template('ads.html', {'ads': ads})
        
class NewAd(BaseHandler):

    def post(self):
        ad = Ads(author=self.request.get('inputAuthor'),
                  text=self.request.get('inputText'),
                  priority=int(self.request.get('inputPriority')))
        ad.put()
        return webapp2.redirect('/')

    def get(self):
        self.render_template('new.html', {})


class EditAd(BaseHandler):

    def post(self, ad_id):
        iden = int(ad_id)
        # ad = db.get(db.Key.from_path('Ads', iden))
        key = ndb.Key('Ads', iden)
        ad = key.get()
        ad.author = self.request.get('inputAuthor')
        ad.text = self.request.get('inputText')
        ad.priority = int(self.request.get('inputPriority'))
        ad.date = datetime.now()
        ad.put()
        
        return webapp2.redirect('/')

    def get(self, ad_id):
        iden = int(ad_id)
        
        # ad = db.get(db.Key.from_path('Ads', iden))
        key = ndb.Key('Ads', iden)
        ad = key.get()
        self.render_template('edit.html', {'ad': ad})


class DeleteAd(BaseHandler):

    def get(self, ad_id):
        iden = int(ad_id)
        # ad = db.get(db.Key.from_path('Ads', iden))
        key = ndb.Key('Ads', iden)
        key.delete()
        return webapp2.redirect('/')


