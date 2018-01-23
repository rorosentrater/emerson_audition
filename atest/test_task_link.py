from unittest import TestCase
from qat.utils import Decorators

from selenium.webdriver.common.by import By


class TaskLink(TestCase):

    def setup(self, driver, arguments):
        browser = driver(**arguments)
        browser.get('https://riot-todo-84334.firebaseapp.com/#!/')
        return browser

    @Decorators.browsers()
    def test_new_task(self, driver, arguments):
        """Creates a new task"""
        browser = self.setup(driver, arguments)
        # Checks/sets count of initial number of tasks
        before_count = len(browser.find_elements(By.CSS_SELECTOR, 'todo-list  li'))
        # Fills out the Assignee field with some text
        browser.find_element(By.ID, 'taskAssignee').send_keys('Logan')
        # Fills out the Title field with some text
        browser.find_element(By.ID, 'taskTitle').send_keys('Shopping List')
        # Fills out the Content field with some text
        browser.find_element(By.ID, 'taskContent').send_keys('Milk, Eggs, Cheese')
        # Click the Create Button to Create the task
        browser.find_element(By.CSS_SELECTOR, 'create-todo button').click()
        # Checks/sets count number of task after adding the new task
        after_count = len(browser.find_elements(By.CSS_SELECTOR, 'todo-list  li'))
        # Gets the list of current tasks
        current_tasks = browser.find_elements(By.CSS_SELECTOR, 'todo-list  li')
        # Compares to ensure a task was added
        self.assertEqual(after_count, before_count + 1)
        # Finds the new task's link and navigates to the assignees profile
        current_tasks[-1].find_element(By.CSS_SELECTOR, 'todo-task span:nth-of-type(2)').click()
        # Ensures the correct profile/URL has been navigated to
        self.assertEqual(browser.current_url, 'https://riot-todo-84334.firebaseapp.com/#!/profile/Logan')
        browser.quit()
