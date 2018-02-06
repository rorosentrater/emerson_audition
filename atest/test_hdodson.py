from unittest import TestCase
from qat.utils import Decorators
from library.qat.todo.hd_todo import Task


class TaskTest(TestCase):

    def create_controller(self, driver, arguments, link):
        browser = driver(**arguments) if arguments else driver()
        controller = Task(browser, link)
        return controller

    @Decorators.browsers()
    def test_task_create(self, driver, arguments):
        controller = self.create_controller(driver, arguments, 'https://riot-todo-84334.firebaseapp.com/#!/')
        task_count = controller.components.home.task_elements.count()
        controller.task_create('Lee', 'Nothing to do here', 'Seriously')
        self.assertEqual(controller.components.home.task_elements.count(), task_count + 1)
        controller.exit()

    @Decorators.browsers(development=True)
    def test_assignee_link(self, driver, arguments):
        controller = self.create_controller(driver, arguments, 'https://riot-todo-84334.firebaseapp.com/#!/')
        task_id = controller.task_create('Lee', 'Nothing to do here', 'Seriously')
        controller.components.home.task_details.fmt(id=task_id).assignee.click()
        self.assertTrue(controller.is_location('https://riot-todo-84334.firebaseapp.com/#!/profile/Lee',
                                               timeout=5,
                                               strict=True))
        controller.exit()

    @Decorators.browsers()
    def test_task_delete(self, driver, arguments):
        controller = self.create_controller(driver, arguments, 'https://riot-todo-84334.firebaseapp.com/#!/')
        task_id = controller.task_create('The Assignee', 'The Title', 'The Content')
        controller.task_delete(task_id)
        controller.exit()
