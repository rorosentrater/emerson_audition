from pyscc import Component, component_element, component_group


class Homepage(Component):

    @component_element
    def logo(self):
        return 'div.navbar-header'
