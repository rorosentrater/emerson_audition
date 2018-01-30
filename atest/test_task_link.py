from unittest import TestCase
from qat.utils import Decorators
from library.qat.todo.lk_todo import App


class TaskLink(TestCase):

    def setup(self, driver, arguments):
        browser = driver(**arguments)
        controller = App(browser, "https://riot-todo-84334.firebaseapp.com/#!/")
        return controller

    @Decorators.browser(name='chrome')
    def test_create(self, driver, arguments):
        """Creates a new task"""
        browser = self.setup(driver, arguments)
        browser.task_create('Logan', 'Shopping List', 'Milk, Eggs, Cheese')

    @Decorators.browser(name='chrome')
    def test_delete(self, driver, arguments):
        """Deletes a task"""
        browser = self.setup(driver, arguments)
        browser.task_delete()
