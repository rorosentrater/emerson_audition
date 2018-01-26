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
        create_default_task(self.driver, "Lee", "Nothing to do here", "Seriously")
        # Confirms a new task was created
        self.assertTrue(self.driver.find_element_by_css_selector("li.animated.fadeIn:nth-child({})".format(count + 1)))

    def test_assignee_link(self):
        # Create a new task
        create_default_task(self.driver, "Lee", "Nothing to do here", "Seriously")
        # Click assignee profile
        assignee_elements = self.driver.find_elements_by_css_selector("span#assignee")
        assignee_elements[-1].click()
        # Confirm I am on the expected profile page
        self.assertEqual(self.driver.current_url, "https://riot-todo-84334.firebaseapp.com/#!/profile/Lee")

    def tearDown(self):
        self.driver.quit()


def create_default_task(web_driver, assignee, title, content):
    web_driver.find_element_by_css_selector("#taskAssignee").send_keys(assignee)
    web_driver.find_element_by_css_selector("#taskTitle").send_keys(title)
    web_driver.find_element_by_css_selector("#taskContent").send_keys(content)
    web_driver.find_element_by_css_selector(".is-success.u-pull-right").click()
