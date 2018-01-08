from pyscc import Controller
from .components import Page


class App(Controller):

    def foobar(self):
        return 'hello world'
