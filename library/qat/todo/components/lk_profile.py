from pyscc import Component, component_element


class Profile(Component):

    @component_element
    def profile(self):
        return 'r-view'

    @component_element
    def name(self):
        return 'r-view > profile > h1'

    @component_element
    def latest_task(self):
        return 'r-view > profile > h4'

    @component_element
    def task_link(self):
        return 'r-view > profile > h4 > a'

    @component_element
    def stat_header(self):
        return 'r-view > profile > h4 > a'

    @component_element
    def stats(self):
        return '#stats'
