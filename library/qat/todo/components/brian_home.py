# pylint: disable=no-self-use
from pyscc import Component, \
    component_element, component_elements, component_group


class BrianHome(Component):

    @component_elements
    def link(self):
        return '#assignee'

    @component_element
    def button(self):
        return 'button'

    @component_element
    def task_assignee(self):
        return "#taskAssignee"

    @component_element
    def task_title(self):
        return "#taskTitle"

    @component_element
    def task_content(self):
        return "#taskContent"

    @component_element
    def form_submit(self):
        return ".is-success.u-pull-right"

    @component_element
    def prof_label(self):
        return "r-view > profile > h1"

    @component_element
    def task_label(self):
        return "h4 > a"
