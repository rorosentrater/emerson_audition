from pyscc import Controller
from components import BrianHome


class BrianApp(Controller):

    def __init__(self, browser, url):
        """
        :Description: Controller used for testing Todo input forms.
        :param browser: Selenium browser reference to pass to referenced page and modal objects.
        :type browser: webdriver
        :param url: Base url used to navigate with your controller.
        :type url: basestring
        """
        super(BrianApp, self).__init__(browser, url, {
            'home': BrianHome
        })

    def link_path(self):
        """
        :Description: Navigates to task and verifies correct URL.
        """
        self.components.home.link.get()[self.count - 1].click()
        assert self.instance_assignee in self.location

    def form_fill(self, assignee, title, content):
        """
        :Description: Sends input to forms to test their functionality.
        :param assignee: string to pass to forms.
        :type assignee: string.
        :param title: string to pass to forms.
        :type title: string.
        :param content: string to pass to forms.
        :type content: string.
        """
        home = self.components.home
         #pylint: disable=attribute-defined-outside-init
        self.count = home.link.count()
        self.instance_assignee = assignee
        self.instance_title = title
        home.form.form_assignee.send_input(assignee)
        home.form.form_title.send_input(title)
        home.form.form_content.send_input(content)
        home.form.form_submit.click()
        assert self.count < home.link.count()
        self.count = home.link.count()

    def task_check(self):
        """
        :Description: Verifies that the assignee page reflects the input.
        """
        home = self.components.home
        assert self.instance_assignee in home.prof_label.text(raw=True)
        assert self.instance_title in home.task_label.text(raw=True)
