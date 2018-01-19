# pylint: disable=no-self-use
from pyscc import Component, \
    component_element, component_elements, component_group


class BrianHome(Component):


    @component_group
    def form(self):
        return {'form_assignee': '#taskAssignee', 'form_title': '#taskTitle',
                'form_content': "#taskContent",
                "form_submit": ".is-success.u-pull-right"}

    @component_elements
    def link(self):
        return '#assignee'

    @component_element
    def button(self):
        return 'button'

    @component_element
    def prof_label(self):
        return "r-view > profile > h1"

    @component_element
    def task_label(self):
        return "h4 > a"
