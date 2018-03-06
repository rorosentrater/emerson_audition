from unittest import TestCase
from atest._setup_ import Setup
from selenium import webdriver
import time


class CategoryCategory(TestCase):

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
        """Checks that some specific options in the conditions category are visible"""
        self.controller.components.header.header_option.shop\
            .wait_for(5, error='Shop dropdown button did not render as expected')\
            .get().click()  # Open shop dropdown
        self.controller.components.header.shop_categories.category.wait_visible(
            5, error='"category" category did not render as expected. Dropdown may not have been opened')\
            .get().click()
        self.controller.components.header.shop_category_nutritional_sups.amino_acids.wait_visible(5, error=True)
        self.controller.components.header.shop_category_nutritional_sups.herbal_products.wait_visible(5, error=True)
        self.controller.components.header.shop_category_addl_options.household_ess.wait_visible(5, error=True)

    def test_check_all_options(self):
        """Checks that all options in the conditions category are visible"""
        self.controller.components.header.header_option.shop \
            .wait_for(5, error='Shop dropdown button did not render as expected') \
            .get().click()  # Open shop dropdown
        self.controller.components.header.shop_categories.category.wait_visible(
            5, error='"category" category did not render as expected. Dropdown may not have been opened')\
            .get().click()
        self.assertTrue(
            self.controller.wait(
                timeout=5,
                condition=self.controller.components.header.shop_category_nutritional_sups.check.visible
            ), 'Not all options were visible'
        )
        self.assertTrue(
            self.controller.wait(
                timeout=5,
                condition=self.controller.components.header.shop_category_addl_options.check.visible
            ), 'Not all options were visible'
        )

    def test_option_opens_search(self):
        """Checks that we are brought to a search results page after clicking an option"""
        self.controller.components.header.header_option.shop \
            .wait_for(5, error='Shop dropdown button did not render as expected') \
            .get().click()  # Open shop dropdown
        self.controller.components.header.shop_categories.category.wait_visible(
            5, error='"category" category did not render as expected. Dropdown may not have been opened')\
            .get().click()
        self.controller.components.header.shop_category_addl_options.household_ess.wait_visible(5, error=True).click()
        self.controller.verify_search_boiler_plate()
        # We passed the boilerplate check, now make sure "Household Essentials" was the auto-filled search term.
        result_text = self.controller.components.search.x_returned_y_results\
            .wait_for(5, error=True)\
            .text()
        self.assertIn(
            member='Household Essentials',
            container=result_text,
            msg='Expected the string "Eye Ear Support" to be in the returned results text. "%s" was found instead'
                % result_text
        )

    # Negative tests (I built these to fail on purpose but hopefully making "believable" mistakes)
    def test_failure_to_open(self):
        """Checks that we are brought to a search results page after clicking an option"""
        # This is going to dispatch a raw JS click event on the shop header button. This does not open the dropdown.
        # I suspect this is because our raw JS click lacks any event bubbling but whatever the reason, its a common
        # mistake I thought would be good to give an example of.
        self.controller.components.header.header_option.shop \
            .wait_for(5, error='Shop dropdown button did not render as expected') \
            .click()
        self.controller.components.header.shop_categories.category.wait_visible(
            5, error='"category" category did not render as expected. Dropdown may not have been opened')

    def test_more_than_expected(self):
        """Go to search results page by clicking 'eyes & ears' but only expect 4 items"""
        self.controller.components.header.header_option.shop \
            .wait_for(5, error='Shop dropdown button did not render as expected') \
            .get().click()  # Open shop dropdown
        self.controller.components.header.shop_categories.category.wait_visible(
            5, error='"category" category did not render as expected. Dropdown may not have been opened')\
            .get().click()
        self.controller.components.header.shop_category_addl_options.household_ess.wait_visible(5, error=True).click()
        self.controller.verify_search_boiler_plate(items=4, strict=True)

    # Performance tests
    # DISCLAIMER: Selenium is not really built for performance/load testing. There are much better tools for doing this.
    # http://elementalselenium.com/tips/48-load-testing
    # It doesnt really make sense to simulate user activities with Selenium since the only thing that matters in the
    # Client server model are the actual http requests, and API performance. Using Selenium in this way is just an
    # overcomplicated way to send glorified requests IMO.
    # That being said, it can be done albeit with a lot of overhead. These tests I wrote are really the only type of
    # selenium based performance measuring tests I believe are "worth it" if you don't want to commit to an API testing
    # suite, but would still like some baseline data on page load times.
    def test_record_search_load_time(self):
        """Checks how long it takes for a webdriver to report it's "ready" state after reloading a page"""
        self.controller.components.header.header_option.shop \
            .wait_for(5, error='Shop dropdown button did not render as expected') \
            .get().click()  # Open shop dropdown
        self.controller.components.header.shop_categories.category.wait_visible(
            5, error='"category" category did not render as expected. Dropdown may not have been opened')\
            .get().click()
        self.controller.components.header.shop_category_addl_options.household_ess\
            .wait_visible(5, error=True)\
            .click()
        start_time = time.time()  # Start timer directly before operation that causes page load
        # Cause one of the FEW operations in Selenium where the browser is responsible for stalling the thread
        self.controller.refresh()  # .get() is another version of this operation.
        #  webdrivers are responsible for reporting page ready state.
        print 'page load took %s seconds' % (time.time()-start_time)  # report on the time elapsed.

    def test_wait_time(self):
        """
        Description: Checks how long it takes a given function to run
        # So this is an imperfect performance test. what we are doing here is reporting how long the method
        # "verify_search_boiler_plate" took to run. I chose to check a group of elements on purpose (more on that later)
        # Now because we have to wait for elements to load, we are using our component/implicit waits. This is going
        # to limit our results to within a one second margin of error for a single element and adding an addition second
        # of error for each subsequent element waited on before stopping the timer (because availability checks are only
        # run once a second). Lowering our minimum wait intervals would shrink our margin of error right?
        # It would, but at a HUGE performance cost. Every time we ask Selenium to check for the existence of an element,
        # a request is sent to the grid/node/webdriver. Spamming requests like this will give your node the hug of death
        # OR in a worst case scenario, because webdrivers are often run in parallel on nodes, if they dont die outright,
        # the added CPU load would skew your results, making every operation appear to take much longer than it actually
        # would otherwise. The only "kind of" useful information you can get from measuring load times is by measuring
        # the load times of "groups" of elements. You can expect a group of elements to load in a certain amount of time
        # and a test like this would let you know if you were under that number. If you however go OVER that tolerated
        # amount of time, but each individual element was withing its own personal timeout toleration, there's no way to
        # tell what the problem element is.
        """
        self.controller.components.header.header_option.shop \
            .wait_for(5, error='Shop dropdown button did not render as expected') \
            .get().click()  # Open shop dropdown
        self.controller.components.header.shop_categories.category.wait_visible(
            5, error='"category" category did not render as expected. Dropdown may not have been opened')\
            .get().click()
        self.controller.components.header.shop_category_addl_options.household_ess.wait_visible(5, error=True).click()
        start_time = time.time()  # Start timer directly before operation that causes page load
        self.controller.verify_search_boiler_plate()
        print 'search page boiler plate elements loaded in %s seconds' \
              % (time.time()-start_time)  # report on the time elapsed.
