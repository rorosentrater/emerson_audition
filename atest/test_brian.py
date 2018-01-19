from unittest import TestCase
from selenium import webdriver


from library.qat.todo import BrianApp
from qat.utils import Decorators


class BrianTestTodo(TestCase):

    @Decorators.browsers()
    def test_form_fill(self, driver, arguments):
        """
         :Description: Verifies that task creation form works.
         """
        browser = driver(**arguments)
        browser.get('https://riot-todo-84334.firebaseapp.com/#!/"') if arguments else driver()
        controller = BrianApp(browser, "https://riot-todo-84334.firebaseapp.com/#!/")
        controller.form_fill("Brian", "clean out chicken coop", "they smell bad")
        controller.exit()

    @Decorators.browsers()
    def test_link(self, driver, arguments):
        """
        :Description: Creates a task, follows assignee link and verifies url + page text.
        """
        browser = driver(**arguments) if arguments else driver()
        browser.get('https://riot-todo-84334.firebaseapp.com/#!/"') if arguments else driver()
        controller = BrianApp(browser, "https://riot-todo-84334.firebaseapp.com/#!/")
        controller.form_fill("Walter", "Clean the methlab", "There is a barrel leaking in there!")
        controller.link_path("Walter")
        controller.task_check("Walter", "Clean the methlab")
        controller.exit()

    def test_todo_bl(self):
        """
        :Description: Verifies elements of todo.
        """
        driver = webdriver.Firefox()
        driver.get("https://riot-todo-84334.firebaseapp.com/#!/")
        driver.find_element_by_id("task-1")
        driver.find_element_by_id("task-2")
        driver.find_element_by_id("task-3")
        driver.find_element_by_class_name("is-danger.u-pull-left")
        driver.find_element_by_class_name("is-success.u-pull-right")
        driver.find_element_by_class_name("ico.ico-mat.fi-social-twitter")
        driver.find_element_by_class_name("ico.ico-mat.fi-social-linkedin")
        driver.find_element_by_class_name("ico.ico-mat.fi-social-github")
        driver.close()
