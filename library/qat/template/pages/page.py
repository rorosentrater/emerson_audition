# pylint: disable=no-self-use, unused-import
from pyscc import Component, \
    component_element, component_elements, component_group


class Page(Component):

    @component_element
    def button(self):
        return 'button'
