# pylint: disable=no-self-use
from pyscc import Component, \
    component_element, component_elements, component_group


class Page(Component):

    @component_element
    def button(self):
        return 'button'

    @property
    def task_assignee(self):
        return self.browser.find_element_by_id("taskAssignee")

    @property
    def task_title(self):
        return self.browser.find_element_by_id("taskTitle")

    @property
    def task_content(self):
        return self.browser.find_element_by_id("taskContent")

    @property
    def form_submit(self):
        return self.browser.find_element_by_class_name("is-success.u-pull-right")


    def task(self, index):
        param = "li:nth-of-type(" + str(index) + ")"
        return self.browser.find_element_by_css_selector(param)
