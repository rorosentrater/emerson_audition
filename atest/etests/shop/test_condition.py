from unittest import TestCase
from atest._setup_ import Setup
from selenium import webdriver



class TaskLink(TestCase):

    def setUp(self):
        """Makes a controller instance and navigates to the website"""
        # Normally we would be passing the driver and driver-arguments dynamically using env vars, but for this example
        # we will just use chrome with no arguments
        driver = webdriver.Chrome()
        self.controller = Setup().setup_func(driver)

    def tearDown(self):
        """Closes Browser"""
        self.controller.browser.quit()

    def test_check_specific_options(self):
        """Checks that some specific options in the conditions category are visible"""
        self.controller.components.header.header_option.shop\
            .wait_for(5, error='Shop dropdown button did not render as expected')\
            .get().click()  # Open shop dropdown
        self.controller.components.header.shop_categories.condition.wait_visible(
            5, error='"Condition" category did not render as expected. Dropdown may not have been opened')
        self.controller.components.header.shop_condition_options.womens_health.wait_visible(5, error=True)
        self.controller.components.header.shop_condition_options.Mens_Health.wait_visible(5, error=True)
        self.controller.components.header.shop_condition_options.eye_and_ear.wait_visible(5, error=True)

    def test_check_all_options(self):
        """Checks that all options in the conditions category are visible"""
        self.controller.components.header.header_option.shop \
            .wait_for(5, error='Shop dropdown button did not render as expected') \
            .get().click()  # Open shop dropdown
        self.controller.components.header.shop_categories.condition.wait_visible(
            5, error='"Condition" category did not render as expected. Dropdown may not have been opened')
        self.assertTrue(
            self.controller.wait(
                timeout=5,
                condition=self.controller.components.header.shop_condition_options.check.visible
            ), 'Not all options were visible'
        )

    def test_option_opens_search(self):
        self.controller.components.header.header_option.shop \
            .wait_for(5, error='Shop dropdown button did not render as expected') \
            .get().click()  # Open shop dropdown
        self.controller.components.header.shop_categories.condition.wait_visible(
            5, error='"Condition" category did not render as expected. Dropdown may not have been opened')
        self.controller.components.header.shop_condition_options.eye_and_ear.wait_visible(5, error=True).click()







