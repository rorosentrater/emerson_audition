from pyscc import Controller
from components.brian_home import LinkElements


class LinkTestController(Controller):

    def __init__(self, browser, url):
        """:Description: Controller used for testing Todo input forms.
        :param browser: Selenium browser reference to pass to referenced page and modal objects.
        :type browser: webdriver
        :param url: Base url used to navigate with your controller.
        :type url: basestring
        """
        super(LinkTestController, self).__init__(browser, url, {})
        self.elements = LinkElements(self)

    def link_path(self):
        """:Description: Navigates to task and verifies correct URL.
        """
        self.elements.link.get()[self.count].click()
        assert self.instance_assignee in self.location

    def form_fill(self, assignee, title, content):
        """:Description: Sends input to forms to test there functionality.
        :param assignee: string to pass to forms.
        :type assignee: string.
        :param title: string to pass to forms.
        :type title: string.
        :param content: string to pass to forms.
        :type content: string.
        """
        self.count = self.elements.link.count()
        self.instance_assignee = assignee
        self.instance_title = title
        self.elements.task_assignee.send_input(assignee)
        self.elements.task_title.send_input(title)
        self.elements.task_content.send_input(content)
        self.elements.form_submit.click()

    def task_check(self):
        """:Description: Verifies that the assignee page reflects the input.
        """
        assert self.instance_assignee in self.elements.prof_label.text(raw=True)
        assert self.instance_title in self.elements.task_label.text(raw=True)
