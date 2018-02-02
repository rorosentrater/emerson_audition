from unittest import TestCase
from qat.utils import Decorators
from library.qat.todo.hd_todo import Task


class TaskTest(TestCase):

    @Decorators.browsers()
    def test_task_create(self, driver, arguments):
        controller = create_controller(driver, arguments, 'https://riot-todo-84334.firebaseapp.com/#!/')
        task_count = controller.components.home.task_elements.count()
        controller.task_create('Lee', 'Nothing to do here', 'Seriously')
        self.assertTrue(controller.components.home.task_elements.count(), task_count + 1)
        controller.exit()

    @Decorators.browsers()
    def test_assignee_link(self, driver, arguments):
        controller = create_controller(driver, arguments, 'https://riot-todo-84334.firebaseapp.com/#!/')
        controller.task_create('Lee', 'Nothing to do here', 'Seriously')
        task_count = controller.components.home.task_elements.count()
        controller.components.home.task_details.fmt(index=task_count).assignee.click()
        controller.wait(1)
        self.assertEqual(controller.location, 'https://riot-todo-84334.firebaseapp.com/#!/profile/Lee')
        controller.exit()

    @Decorators.browsers()
    def test_task_delete(self, driver, arguments):
        controller = create_controller(driver, arguments, 'https://riot-todo-84334.firebaseapp.com/#!/')
        # Create a new task
        controller.task_create('The Assignee', 'The Title', 'The Content')
        task_count = controller.components.home.task_elements.count()
        # Delete the created task
        controller.task_delete(task_count)
        controller.wait(1)
        # Confirm at least one task was removed
        self.assertTrue(task_count > controller.components.home.task_elements.count())
        controller.exit()


def create_controller(driver, arguments, link):
    browser = driver(**arguments) if arguments else driver()
    controller = Task(browser, link)
    return controller
