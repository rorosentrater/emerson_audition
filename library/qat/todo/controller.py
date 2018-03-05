from pyscc import Controller
from components.emerson_homepage import Homepage
from components.emerson_header import Header
from components.emerson_search_page import SearchResults


class Emc(Controller):

    def __init__(self, browser, base_url):
        """
        :description: Referencing the controller constructor. This controller serves as the repository for any shared
        functions and webelement/component repositories (pages).
        :param browser: Reference to the webdriver
        :type browser: Selenium Webdriver object
        :param base_url: This is the URL we initially go to.
        :type base_url: basestring

        """
        # This is where you init all of you pages so you can access all the web components
        super(Emc, self).__init__(browser, base_url, {
            'home': Homepage,
            'header': Header,
            'search': SearchResults
        })

    def verify_search_boiler_plate(self, items=1, strict=False):
        """
        :Description: Verifies that search page boiler plate elements loaded
        :param items: How many items you expect to be loaded into the results.
        :type items: int
        :param strict: When set, checks that only EXACTLY the amount of items expected were loaded in.
        :type strict: bool
        """
        self.components.search.filter_results_button.wait_for(5, error='Filter your results button did not render')
        self.components.search.clear_all_button.wait_for(5, error='Clear all button did not render')
        if not self.wait(
            timeout=5,
            condition=self.components.search.master_categories.check.available
        ):
            raise RuntimeError('Not all master filter categories loaded as expected')
        self.components.search.product_items.wait_for(
            timeout=5,
            length=items,
            strict=strict,
            error=True
        )

