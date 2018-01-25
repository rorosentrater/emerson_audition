from selenium import webdriver
from unittest import TestCase


class HomepageRendering(TestCase):

    def test_element_rendering(self):
        driver = webdriver.Firefox()
        driver.get("https://riot-todo-84334.firebaseapp.com/#!/")

        # Confirm To-Do render
        self.assertTrue(driver.find_element_by_css_selector(".logo.animated.slideInDown"))
        # Confirm Social Media links render
        self.assertTrue(driver.find_element_by_css_selector(".fi-social-twitter"))
        self.assertTrue(driver.find_element_by_css_selector(".fi-social-linkedin"))
        self.assertTrue(driver.find_element_by_css_selector(".fi-social-github"))
        # Confirm tasks render
        self.assertTrue(driver.find_element_by_css_selector("#task-1"))
        self.assertTrue(driver.find_element_by_css_selector("#task-2"))
        self.assertTrue(driver.find_element_by_css_selector("#task-3"))
        # Confirm create task button renders
        self.assertTrue(driver.find_element_by_css_selector(".is-success.u-pull-right"))
        # Confirm deleted completed task button renders
        self.assertTrue(driver.find_element_by_css_selector(".is-danger.u-pull-left"))

        driver.quit()
