from pyscc import Controller
from components.lk_home import Home
from components.lk_profile import Profile
from components.lk_header import Header


class App(Controller):

    def __init__(self, browser, base_url):
        """Referencing the controller constructor"""
        super(App, self).__init__(browser, base_url, {
            'home': Home,
            'header': Header,
            'profile': Profile
        })

    def task_delete(self):
        """Tests & Verifies task deletion"""
        before = self.components.home.items.count()
        self.components.home.task.delete.click()
        self.components.home.items.wait_for(1, before - 1, error=True)

    def task_create(self, assignee, title, content):
        """Tests & Verifies task creation"""
        before = self.components.home.items.count()
        self.components.home.create.assignee.send_input(assignee)
        self.components.home.create.title.send_input(title)
        self.components.home.create.content.send_input(content)
        self.components.home.create.create.click()
        self.components.home.items.wait_for(1, before + 1, error=True)
