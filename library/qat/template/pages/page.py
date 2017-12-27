# pylint: disable=no-self-use
from pyscc import Component, \
    component_element, component_elements, component_group


class Page(Component):

    @component_element
    def login_button(self):
        return 'button#login'

    @component_elements
    def users(self):
        return 'ul.users > li a'

    @component_group
    def user_menu(self):
        return {
            'logout': 'a#logout',
            'profile': 'a#profile'
        }
