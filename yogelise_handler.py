import logging
from oloso_handler import * #import all from oloso_handler file
import datetime

class HomeHandler(Oloso):
  def get(self): #all rendering 
    self.RenderTemplate(
      'text/html', 
      'html/index.html',
      {'the_time': datetime.datetime.now()}
    )


def Handler404(request, response, exception):
  logging.exception(exception)
  response.write('Ruh roh! You has an error. Prease fix :(')
  response.set_status(404)
