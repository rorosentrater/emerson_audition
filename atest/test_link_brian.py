from unittest import TestCase
from selenium import webdriver
from library.qat.todo.brian_todo import LinkTestController


class TestLink(TestCase):

    def test_link(self):
        """:Description: Creates a task, follows assignee link and verifies url + page text.
        """

        my_driver = webdriver.Firefox()
        controller = LinkTestController(my_driver, "https://riot-todo-84334.firebaseapp.com/#!/")
        controller.form_fill("Walter", "Clean the methlab", "There is a barrel leaking in there!")
        controller.link_path()
        controller.task_check()
        controller.exit()

