__author__ = 'nat'

from base import BaseRequestHandler


class MainHandler(BaseRequestHandler):
  def get(self):
    self.render("home.html")
