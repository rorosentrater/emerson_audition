from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoganTestTodo(TestCase):

    def setUp(self):
        """Creates Firefox Webdriver instance"""
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.emersonecologics.com/')

    # def test_page_render(self):
    #     """Calls test_rendered on necessary elements to verify they render as expected"""
    #     driver = webdriver.Firefox()
    #     driver.get("https://riot-todo-84334.firebaseapp.com/#!/")
    #     assert driver.find_element(By.ID, "deleteTasks")
    #     # Verifies Delete Completed Button renders correctly
    #     assert driver.find_element(By.CLASS_NAME, "is-success.u-pull-right")
    #     # Verifies Create Task Button renders correctly
    #     assert driver.find_element(By.ID, "social")
    #     # Verifies list of Social widgets renders correctly
    #     assert driver.find_element(By.CLASS_NAME, "logo.animated.slideInDown")
    #     # Verifies To-Do header renders correctly
    #     assert driver.find_element(By.CLASS_NAME, "unstyled")
    #     # Verifies list of Tasks renders correctly
    #     driver.quit()
    #     # Terminates Webdriver

    def test_create_task(self):
        """Creates a new task"""
        print 'garb'

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
        self.driver.find_element(By.CSS_SELECTOR, 'li:nth-of-type(4)')
        # Checks for the newly created fourth task

    def test_new_task(self):
        """Creates a new task"""
        # Checks/sets count of initial number of tasks
        before_count = len(self.task_list())
        # Fills out the Assignee field with some text
        self.driver.find_element(By.ID, 'taskAssignee').send_keys('Logan')
        # Fills out the Title field with some text
        self.driver.find_element(By.ID, 'taskTitle').send_keys('Shopping List')
        # Fills out the Content field with some text
        self.driver.find_element(By.ID, 'taskContent').send_keys('Milk, Eggs, Cheese')
        # Click the Create Button to Create the task
        self.driver.find_element(By.CLASS_NAME, 'is-success.u-pull-right').click()
        # Checks/sets count number of task after adding the new task
        after_count = len(self.task_list())
        # Gets the list of current tasks
        current_tasks = (self.task_list())
        # Compares to ensure a task was added
        self.assertEqual(after_count, before_count + 1)
        # Finds the new task's link and navigates to the assignees profile
        current_tasks[-1].find_element(By.CSS_SELECTOR, 'todo-task span:nth-of-type(2)').click()
        # Ensures the correct profile/URL has been navigated to
        self.assertEqual(
            self.driver.current_url, 'https://riot-todo-84334.firebaseapp.com/#!/profile/Logan')

    def task_list(self):
        """Gets count of the number of tasks"""
        return self.driver.find_elements(By.CSS_SELECTOR, 'todo-list  li')

    def tearDown(self):
        """Closes Browser"""
        self.driver.quit()
