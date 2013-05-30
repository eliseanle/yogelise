import os 
import webapp2 as webapp 

from google.appengine.ext.webapp import template 

class Oloso(webapp.RequestHandler):
  def RenderTemplate(self, content_type, template_name, template_values):
    path = os.path.join(os.path.dirname(__file__), template_name)
    self.response.headers['Content-Type'] = content_type
    self.response.out.write(template.render(path, template_values))

##all above is stock