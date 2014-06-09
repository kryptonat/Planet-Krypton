__author__ = 'nat'

from base import BaseRequestHandler


class HomepageHandler(BaseRequestHandler):
  def get(self):
    self.render("home.html")

class ContactHandler(BaseRequestHandler):
  def get(self):
    self.render("contact.html")

class AboutHandler(BaseRequestHandler):
  def get(self):
    self.render("about.html")
