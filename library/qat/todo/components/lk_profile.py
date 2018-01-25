from pyscc import Component, component_element,  component_group


class Profile(Component):

    @component_element
    def logo(self):
        return 'a h1.logo.animated.slideInDown'

    @component_group
    def social(self):
        return {
            'social': '#social',
            'twitter': 'a i.ico.ico-mat.fi-social-twitter',
            'linkedin': 'a i.ico.ico-mat.fi-social-linkedin',
            'github': 'a i.ico.ico-mat.fi-social-github'
        }

    @component_group
    def profile(self):
        return {
            'profile': 'r-view',
            'name': 'r-view > profile > h1',
            'latest_task': 'r-view > profile > h4',
            'task_link': 'r-view > profile > h4 > a',
            'stat_header': 'r-view > profile > h2',
            'stats': '#stats'
        }
