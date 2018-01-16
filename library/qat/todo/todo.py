from pyscc import Controller
from .components import Page


class App(Controller):

    def __init__(self, browser, url):

        super(App, self).__init__(browser, url, {})
        self.my_page = Page(self)

    def form_fill_out(self, a, b, c):

        self.my_page.task_assignee.send_input(a)
        self.my_page.task_title.send_input(b)
        self.my_page.task_content.send_input(c)
        self.my_page.form_submit.click()

    def task_created(self, expected):
        assert expected == self.my_page.task.count()
        #self.my_page.task.wait_for(5, length=expected, strict=True, error=True)
