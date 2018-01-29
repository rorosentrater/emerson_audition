from unittest import TestCase
from qat.utils import Decorators


# Exercise 3
class TaskCreation(TestCase):

    @Decorators.browsers()
    def test_creation(self, driver, arguments):
        browser = create_browser_driver(driver, arguments, "https://riot-todo-84334.firebaseapp.com/#!/")
        # Gets the number of current tasks
        count = len(browser.find_elements_by_css_selector("li.animated.fadeIn"))
        # Create a new task
        create_default_task(browser, "Lee", "Nothing to do here", "Seriously")
        # Confirms a new task was created
        self.assertTrue(browser.find_element_by_css_selector("li.animated.fadeIn:nth-child({})".format(count + 1)))
        browser.quit()

    @Decorators.browsers()
    def test_assignee_link(self, driver, arguments):
        browser = create_browser_driver(driver, arguments, "https://riot-todo-84334.firebaseapp.com/#!/")
        # Create a new task
        create_default_task(browser, "Lee", "Nothing to do here", "Seriously")
        # Click assignee profile
        assignee_elements = browser.find_elements_by_css_selector("span#assignee")
        assignee_elements[-1].click()
        # Confirm I am on the expected profile page
        self.assertEqual(browser.current_url, "https://riot-todo-84334.firebaseapp.com/#!/profile/Lee")
        browser.quit()


def create_default_task(web_driver, assignee, title, content):
    web_driver.find_element_by_css_selector("#taskAssignee").send_keys(assignee)
    web_driver.find_element_by_css_selector("#taskTitle").send_keys(title)
    web_driver.find_element_by_css_selector("#taskContent").send_keys(content)
    web_driver.find_element_by_css_selector(".is-success.u-pull-right").click()


def create_browser_driver(driver, arguments, link):
    browser = driver(**arguments)  # if arguments else driver()
    browser.get(link)
    return browser
