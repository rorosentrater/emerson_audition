from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from library.qat.todo import App


class VerifyRender(TestCase):

    def test_page_render(self):
        """Calls test_rendered on necessary elements to verify they render as expected"""
        app = App(webdriver.Firefox(), 'https://riot-todo-84334.firebaseapp.com/#!/', {})
        try:
            assert App.test_rendered(app, By.ID, "deleteTasks")
            # Verifies Delete Completed Button renders correctly
            assert App.test_rendered(app, By.CLASS_NAME, "is-success.u-pull-right")
            # Verifies Create Task Button renders correctly
            assert App.test_rendered(app, By.ID, "social")
            # Verifies list of Social widgets renders correctly
            assert App.test_rendered(app, By.CLASS_NAME, "logo.animated.slideInDown")
            # Verifies To-Do header renders correctly
            assert App.test_rendered(app, By.CLASS_NAME, "unstyled")
            # Verifies list of Tasks renders correctly
        finally:
            # Terminates Webdriver"""
            app.browser.quit()
