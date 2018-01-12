from unittest import TestCase
from selenium import webdriver


class TestTodo(TestCase):

    # foobar

    driver = webdriver.Firefox()
    driver.get("https://riot-todo-84334.firebaseapp.com/#!/")

    webtitle = driver.find_element_by_id("task-1")
    tsk2 = driver.find_element_by_id("task-2")
    tsk3 = driver.find_element_by_id("task-3")
    deletebutton = driver.find_element_by_class_name("is-danger.u-pull-left")
    createbutton = driver.find_element_by_class_name("is-success.u-pull-right")

    twitt = driver.find_element_by_class_name("ico.ico-mat.fi-social-twitter")
    linked = driver.find_element_by_class_name("ico.ico-mat.fi-social-linkedin")
    git = driver.find_element_by_class_name("ico.ico-mat.fi-social-github")

    driver.close()
