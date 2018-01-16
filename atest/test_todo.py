from unittest import TestCase
from selenium import webdriver

from selenium.webdriver.common.by import By


class VerifyRender(TestCase):

    def test_page_render(self):
        """Calls test_rendered on necessary elements to verify they render as expected"""
        driver = webdriver.Firefox()
        driver.get("https://riot-todo-84334.firebaseapp.com/#!/")
        assert driver.find_element(By.ID, "deleteTasks")
        # Verifies Delete Completed Button renders correctly
        assert driver.find_element(By.CLASS_NAME, "is-success.u-pull-right")
        # Verifies Create Task Button renders correctly
        assert driver.find_element(By.ID, "social")
        # Verifies list of Social widgets renders correctly
        assert driver.find_element(By.CLASS_NAME, "logo.animated.slideInDown")
        # Verifies To-Do header renders correctly
        assert driver.find_element(By.CLASS_NAME, "unstyled")
        # Verifies list of Tasks renders correctly
        driver.quit()
        # Terminates Webdriver
from selenium import webdriver

from selenium.webdriver.common.by import By


    def test_todo_bl(self):
        driver = webdriver.Firefox()
        driver.get("https://riot-todo-84334.firebaseapp.com/#!/")
class CreateTask(TestCase):

        driver.find_element_by_id("task-1")
        driver.find_element_by_id("task-2")
        driver.find_element_by_id("task-3")
        driver.find_element_by_class_name("is-danger.u-pull-left")
        driver.find_element_by_class_name("is-success.u-pull-right")

        driver.find_element_by_class_name("ico.ico-mat.fi-social-twitter")
        driver.find_element_by_class_name("ico.ico-mat.fi-social-linkedin")
        driver.find_element_by_class_name("ico.ico-mat.fi-social-github")

        driver.close()
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
