from unittest import TestCase
from selenium import webdriver

from selenium.webdriver.common.by import By


class CreateTask(TestCase):

    def setUp(self):
        """Creates Firefox Webdriver instance"""
        self.driver = webdriver.Firefox()
        self.driver.get('https://riot-todo-84334.firebaseapp.com/#!/')

    def test_create_task(self):
        """Creates a new task"""
        self.driver.find_element(By.ID, 'taskAssignee').send_keys('Logan')
        # Fills out the Assignee field with some text
        self.driver.find_element(By.ID, 'taskTitle').send_keys('Shopping List')
        # Fills out the Title field with some text
        self.driver.find_element(By.ID, 'taskContent').send_keys('Milk, Eggs, Cheese')
        # Fills out the Content field with some text
        self.driver.find_element(By.CLASS_NAME, 'is-success.u-pull-right').click()
        # Clicks Create Button to Create the task

    def tearDown(self):
        """Closes Browser"""
        self.driver.quit()
