from pyscc import Component, component_element, component_group


class Header(Component):

    @component_element
    def logo(self):
        return 'a h1.logo.animated.slideInDown'


    @component_group
    def social(self):
        return {
            '_': '#social',
            'twitter': 'a i.ico.ico-mat.fi-social-twitter',
            'linkedin': 'a i.ico.ico-mat.fi-social-linkedin',
            'github': 'a i.ico.ico-mat.fi-social-github'
        }
