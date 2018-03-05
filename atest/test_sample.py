from unittest import TestCase
from _setup_ import Setup



class TaskLink(TestCase):

    def setUp(self):
        """Makes a controller instance and navigates to the website"""
        self.controller = Setup().setup_func()

    def tearDown(self):
        """Closes Browser"""
        self.controller.browser.quit()

    def test_create(self):
        """Creates a new task"""
        self.controller.print_stuff()
        print self.controller.components.header.shop.get()
        self.controller.components.header.shop.get().click()
        print 'hi'


