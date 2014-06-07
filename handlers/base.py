__author__ = 'nat'

import template
import webapp2


class BaseRequestHandler(webapp2.RequestHandler):
  """ Base Request Handler.

  """

  def render(self, tmpl, params=None):
    """ Render."""
    if params is None:
      params = {}

    self.response.write(template.render(tmpl, template_params=params))
