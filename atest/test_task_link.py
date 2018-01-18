from unittest import TestCase
from selenium import webdriver

from selenium.webdriver.common.by import By


class TaskLink(TestCase):

    def setUp(self):
        """Creates Firefox Webdriver instance"""
        self.driver = webdriver.Firefox()
        self.driver.get('https://riot-todo-84334.firebaseapp.com/#!/')

    def test_new_task(self):
        """Creates a new task"""
        self.driver.find_element(By.ID, 'taskAssignee').send_keys('Logan')
        # Fills out the Assignee field with some text
        self.driver.find_element(By.ID, 'taskTitle').send_keys('Shopping List')
        # Fills out the Title field with some text
        self.driver.find_element(By.ID, 'taskContent').send_keys('Milk, Eggs, Cheese')
        # Fills out the Content field with some text
        self.driver.find_element(By.CLASS_NAME, 'is-success.u-pull-right').click()
        # Click the Create Button to Create the task
        self.driver.find_element(By.CSS_SELECTOR, 'li:nth-of-type(4) span:nth-of-type(2)').click()
        # Finds the new task's link and navigates to the assignees profile
        assert self.driver.current_url == 'https://riot-todo-84334.firebaseapp.com/#!/profile/Logan'
        # Ensures the correct profile/URL has been navigated to

    def tearDown(self):
        """Closes Browser"""
        self.driver.quit()
