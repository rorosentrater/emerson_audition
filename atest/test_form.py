from unittest import TestCase
from selenium import webdriver

from library.qat.todo import App


class TestForm (TestCase):

    def test_form_fill(self):
        my_driver = webdriver.Firefox()
        controller = App(my_driver, "https://riot-todo-84334.firebaseapp.com/#!/")
        controller.form_fill_out("Brian", "clean out chicken coop", "they smell bad")

