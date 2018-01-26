from selenium import webdriver
from unittest import TestCase


# Exercise 2
class TaskCreation(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://riot-todo-84334.firebaseapp.com/#!/")

    def test_creation(self):
        # Gets the number of current tasks
        count = len(self.driver.find_elements_by_css_selector("li.animated.fadeIn"))

        # Create a new task
        self.driver.find_element_by_css_selector("#taskAssignee").send_keys("Lee")
        self.driver.find_element_by_css_selector("#taskTitle").send_keys("Nothing to do here")
        self.driver.find_element_by_css_selector("#taskContent").send_keys("Seriously")
        self.driver.find_element_by_css_selector(".is-success.u-pull-right").click()

        # Confirms a new task was created
        self.assertTrue(self.driver.find_element_by_css_selector("li.animated.fadeIn:nth-child({})".format(count+1)))

    def tearDown(self):
        self.driver.quit()

