from unittest import TestCase
from selenium import webdriver


class TestTodo(TestCase):




    def test_toDo(self):
        driver = webdriver.Firefox()
        driver.get("https://riot-todo-84334.firebaseapp.com/#!/")

        assert driver.find_element_by_id("task-1")
        assert driver.find_element_by_id("task-2")
        assert driver.find_element_by_id("task-3")
        assert driver.find_element_by_class_name("is-danger.u-pull-left")
        assert driver.find_element_by_class_name("is-success.u-pull-right")

        assert driver.find_element_by_class_name("ico.ico-mat.fi-social-twitter")
        assert driver.find_element_by_class_name("ico.ico-mat.fi-social-linkedin")
        assert driver.find_element_by_class_name("ico.ico-mat.fi-social-github")

        driver.close()
