from pyscc import Controller
from .components import Page


class App(Controller):

    def __init__(self, browser, url):

        super(App, self).__init__(browser, url, {})
        self.my_page = Page(self)

    def form_fill_out(self, a, b, c):

        self.my_page.task_assignee.send_keys(a)
        self.my_page.task_title.send_keys(b)
        self.my_page.task_content.send_keys(c)
        self.my_page.form_submit.click()

    def task_created(self, index):
        self.my_page.task(index)
