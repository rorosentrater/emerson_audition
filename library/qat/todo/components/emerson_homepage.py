from pyscc import Component, component_element


class Homepage(Component):

    @component_element
    def logo(self):
        return 'div.navbar-header'
