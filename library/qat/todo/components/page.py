# pylint: disable=no-self-use
from pyscc import Component, \
    component_element, component_elements, component_group


class Page(Component):

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

    @component_elements
    def task(self):
        return "todo-task"
