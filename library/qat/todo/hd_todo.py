from pyscc import Controller
from .components.hd_home import Home


class Task(Controller):

    def __init__(self, browser, base_url):
        super(Task, self).__init__(browser, base_url, {'home': Home})

    # Create a new task
    def task_create(self, assignee, title, content):
        home = self.components.home
        home.task_creation.task_assignee.send_input(assignee)
        home.task_creation.task_title.send_input(title)
        home.task_creation.task_content.send_input(content)
        home.task_creation.create_task_button.click()

    # Select and delete the task at a given index
    def task_delete(self, index):
        home = self.components.home
        home.task_details.fmt(index=index).checkbox.click()
        home.delete_button.click()

    # Returns the current number of tasks
    def task_count(self):
        return self.components.home.task_elements.count()

    def click_assignee(self, index):
        self.components.home.task_details.fmt(index=index).assignee.click()
