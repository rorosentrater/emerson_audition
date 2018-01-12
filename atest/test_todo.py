from unittest import TestCase
from selenium import webdriver


class TestTodo(TestCase):




    def test_todo_bl(self):
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
