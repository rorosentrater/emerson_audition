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

    def link_path(self, assignee):
        """
        :Description: Navigates to task and verifies correct URL.
        :param assignee: string to see if in url.
        :type assignee: string.
        """
        self.components.home.link.get()[-1].click()
        assert assignee in self.location

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
        count = home.link.count()
        home.form.assignee.send_input(assignee)
        home.form.title.send_input(title)
        home.form.content.send_input(content)
        home.form.submit.click()
        assert count < home.link.count()

    def task_check(self, assignee, title):
        """
        :Description: Verifies that the assignee page reflects the input.
        :param assignee: string to verify in task.
        :type assignee: string.
        :param title: string to verify is in task.
        :type title: string
        """
        home = self.components.home
        assert assignee in home.prof_label.text(raw=True)
        assert title in home.task_label.text(raw=True)
