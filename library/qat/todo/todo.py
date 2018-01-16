from pyscc import Controller
from .components import Page


class App(Controller):

    """
    :Description: Controller used for testing Todo input forms.
    :param browser: Selenium browser reference to pass to referenced page and modal objects.
    :type browser: webdriver
    :param base_url: Base url used to navigate with your controller.
    :type base_url: basestring
    :param env: Key value pairs to pass to instantiated components.
    :type env: **kwargs => dict
    """
    def __init__(self, browser, url):

        super(App, self).__init__(browser, url, {})
        self.my_page = Page(self)

    """
    :Description: Sends input to forms to test there functionality.
    :params assignee, title, content: strings to pass to forms.
    :type assignee, title, content: string.
    """
    def form_fill_out(self, assignee, title, content):

        self.my_page.task_assignee.send_input(assignee)
        self.my_page.task_title.send_input(title)
        self.my_page.task_content.send_input(content)
        self.my_page.form_submit.click()

    """
    :Description: Verifies that the correct number of tasks are created.
    :param expected: number of tasks that should exist.
    :type expected: int
    """
    def task_created(self, expected):
        assert expected == self.my_page.task.count()
        #self.my_page.task.wait_for(5, length=expected, strict=True, error=True)
