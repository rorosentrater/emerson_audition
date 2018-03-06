from unittest import TestCase
from atest._setup_ import Setup
from selenium import webdriver


class BrandCategory(TestCase):

    def setUp(self):
        """Makes a controller instance and navigates to the website"""
        # Normally we would be passing the driver and driver-arguments dynamically using env vars, but for this example
        # we will just use chrome with no arguments
        driver = webdriver.Chrome()
        self.controller = Setup().setup_func(driver)

    def tearDown(self):
        """Closes Browser"""
        self.controller.browser.quit()

    # Generic tests
    def test_check_specific_options(self):
        """Checks that some specific button/logos in the brand category are visible"""
        self.controller.components.header.header_option.shop\
            .wait_for(5, error='Shop dropdown button did not render as expected')\
            .get().click()  # Open shop dropdown
        self.controller.components.header.shop_categories.brand.wait_visible(
            5, error='"Brand" category did not render as expected. Dropdown may not have been opened')\
            .get().click()  # Go to Brand category
        self.controller.components.header.shop_brand_options.brand1_logo.wait_visible(5, error=True)
        self.controller.components.header.shop_brand_options.brand1_shop.wait_visible(5, error=True)
        self.controller.components.header.shop_brand_options.a_g.wait_visible(5, error=True)

    def test_check_all_options(self):
        """Checks that all buttons/logos are visible"""
        self.controller.components.header.header_option.shop\
            .wait_for(5, error='Shop dropdown button did not render as expected')\
            .get().click()  # Open shop dropdown
        self.controller.components.header.shop_categories.brand.wait_visible(
            5, error='"Brand" category did not render as expected. Dropdown may not have been opened')\
            .get().click()  # Go to Brand category
        self.controller.components.header.shop_brand_options.brand1_logo.wait_visible(5, error=True)
        self.controller.components.header.shop_brand_options.brand1_shop.wait_visible(5, error=True)
        self.controller.components.header.shop_brand_options.a_g.wait_visible(5, error=True)

