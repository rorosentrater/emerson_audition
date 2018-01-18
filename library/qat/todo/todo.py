from pyscc import Controller
from .components import Page


class App(Controller):
    """:Description: Controller used for testing Todo input forms.
    :param browser: Selenium browser reference to pass to referenced page and modal objects.
    :type browser: webdriver
    :param url: Base url used to navigate with your controller.
    :type url: basestring
    """
    def __init__(self, browser, url):

        super(App, self).__init__(browser, url, {})
        self.my_page = Page(self)

    def form_fill_out(self, assignee, title, content):
        """:Description: Sends input to forms to test there functionality.
        :param assignee: string to pass to forms.
        :type assignee: string.
        :param title: string to pass to forms.
        :type title: string.
        :param content: string to pass to forms.
        :type content: string.
        """
        self.task_count_b4 = self.my_page.task.count()
        self.my_page.task_assignee.send_input(assignee)
        self.my_page.task_title.send_input(title)
        self.my_page.task_content.send_input(content)
        self.my_page.form_submit.click()

    def task_created(self):
        """:Description: Verifies that the correct number of tasks are created.
        """
        assert self.task_count_b4 < self.my_page.task.count()
        #self.my_page.task.wait_for(5, length=expected, strict=True, error=True)
