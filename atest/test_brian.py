from unittest import TestCase
from selenium import webdriver


from library.qat.todo import BrianApp


class BrianTestTodo(TestCase):

    def test_form_fill(self):
        """
         :Description: Verifies that task creation form works.
         """
        my_driver = webdriver.Firefox()
        controller = BrianApp(my_driver, "https://riot-todo-84334.firebaseapp.com/#!/")
        controller.form_fill("Brian", "clean out chicken coop", "they smell bad")
        #controller.task_check()
        controller.exit()

    def test_link(self):
        """
        :Description: Creates a task, follows assignee link and verifies url + page text.
        """
        my_driver = webdriver.Firefox()
        controller = BrianApp(my_driver, "https://riot-todo-84334.firebaseapp.com/#!/")
        controller.form_fill("Walter", "Clean the methlab", "There is a barrel leaking in there!")
        controller.link_path()
        controller.task_check()
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
