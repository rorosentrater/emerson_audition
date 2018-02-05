from unittest import TestCase
from qat.utils import Decorators
from library.qat.todo.hd_todo import Task


class TaskTest(TestCase):

    @Decorators.browsers(development=True)
    def test_task_create(self, driver, arguments):
        controller = create_controller(driver, arguments, 'https://riot-todo-84334.firebaseapp.com/#!/')
        task_count = controller.components.home.task_elements.count()
        controller.task_create('Lee', 'Nothing to do here', 'Seriously')
        self.assertTrue(controller.components.home.task_elements.count(), task_count + 1)
        controller.exit()

    @Decorators.browser(name='firefox', development=True)
    def test_assignee_link(self, driver, arguments):
        controller = create_controller(driver, arguments, 'https://riot-todo-84334.firebaseapp.com/#!/')
        home = controller.components.home
        task_count = controller.components.home.task_elements.count()
        task_id = controller.task_create('Lee', 'Nothing to do here', 'Seriously')
        home.task_elements.wait_for(5, length=task_count + 1, strict=True)
        home.task_details.fmt(id=task_id).assignee.click()
        self.assertEqual(controller.location, 'https://riot-todo-84334.firebaseapp.com/#!/profile/Lee')
        controller.exit()

    @Decorators.browser(name='firefox', development=True)
    def test_task_delete(self, driver, arguments):
        controller = create_controller(driver, arguments, 'https://riot-todo-84334.firebaseapp.com/#!/')
        home = controller.components.home
        task_count = home.task_elements.count()
        task_id = controller.task_create('The Assignee', 'The Title', 'The Content')
        controller.task_delete(task_id)
        controller.wait(1)
        self.assertTrue(task_count > controller.components.home.task_elements.count())
        controller.exit()


def create_controller(driver, arguments, link):
    browser = driver(**arguments) if arguments else driver()
    controller = Task(browser, link)
    return controller
