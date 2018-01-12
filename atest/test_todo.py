from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By


class VerifyRender(TestCase):

    def test_page_render(self):
        """Calls test_rendered on necessary elements to verify they render as expected"""
        self.driver = webdriver.Firefox()
        self.driver.get("https://riot-todo-84334.firebaseapp.com/#!/")
        try:
            assert self.driver.find_element(By.ID, "deleteTasks")
            # Verifies Delete Completed Button renders correctly
            assert self.driver.find_element(By.CLASS_NAME, "is-success.u-pull-right")
            # Verifies Create Task Button renders correctly
            assert self.driver.find_element(By.ID, "social")
            # Verifies list of Social widgets renders correctly
            assert self.driver.find_element(By.CLASS_NAME, "logo.animated.slideInDown")
            # Verifies To-Do header renders correctly
            assert self.driver.find_element(By.CLASS_NAME, "unstyled")
            # Verifies list of Tasks renders correctly
        finally:
            self.driver.quit()
            # Terminates Webdriver
