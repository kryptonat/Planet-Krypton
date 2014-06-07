__author__ = 'nat'

import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(autoescape=True,
                                      loader=jinja2.FileSystemLoader("templates"),
                                      extensions=['jinja2.ext.autoescape'])

def render(template_name, template_params=None):
  template = JINJA_ENVIRONMENT.get_template(template_name)
  return template.render(template_params)
