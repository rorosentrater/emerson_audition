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
        return home.task_elements.get_attribute('id')[-1]

    # Select and delete the task at a given index
    def task_delete(self, task_id, safe_delete=True):
        home = self.components.home
        if not home.task_details.fmt(id=task_id).checkbox.get_property('checked'):
            home.task_details.fmt(id=task_id).checkbox.click()
        if safe_delete:
            for tid in home.task_elements.get_attribute('id'):
                task = home.task_details.fmt(id=tid)
                if tid != task_id and task.checkbox.get_property('checked'):
                    task.checkbox.click()
        home.delete_button.click()
