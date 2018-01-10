# pylint: disable=no-self-use
from pyscc import Component, \
    component_element


class Page(Component):

    @component_element
    def button(self):
        return 'button'
