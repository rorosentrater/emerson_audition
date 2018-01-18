from unittest import TestCase
from selenium import webdriver
from library.qat.todo import BrianApp


class TestForm(TestCase):
    """Description: Test for input todo form.
    """
    def test_form_fill(self):
        my_driver = webdriver.Firefox()
        controller = BrianApp(my_driver, "https://riot-todo-84334.firebaseapp.com/#!/")
        controller.form_fill_out("Brian", "clean out chicken coop", "they smell bad")
        controller.task_created()
        controller.exit()
