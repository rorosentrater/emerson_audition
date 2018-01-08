from pyscc import Controller
from .pages.page import Page


class App(Controller):

    def foobar(self):
        return 'hello world'
