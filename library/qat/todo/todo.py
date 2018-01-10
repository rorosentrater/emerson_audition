from pyscc import Controller
from selenium.common.exceptions import NoSuchElementException


class App(Controller):

    def test_rendered(self, how, what):
        try:
            """Takes parameters to locate an element in the current browser"""
            self.browser.find_element(by=how, value=what)
        except NoSuchElementException:
            """Throws exception if element is not found"""
            return False
        return True
