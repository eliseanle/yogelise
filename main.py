import webapp2 as webapp 
import yogelise_handler 

from google.appengine.ext.webapp.util import run_wsgi_app 
from webapp2_extras.routes import RedirectRoute

application = webapp.WSGIApplication([
  RedirectRoute(r'/', handler='yogelise_handler.HomeHandler', strict_slash = True, name='oloso-home-handler')
  ],debug=True)

application.error_handlers[404] = yogelise_handler.Handler404 

def main():
  run_wsgi_app(application) 

if __name__ == '__main__':
  main()
  
  
# to view in browser: http://127.0.0.1:8080/
##all above is stock