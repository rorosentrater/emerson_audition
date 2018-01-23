from pyscc import Controller
from components import Page


class Product(Controller):
    """
    :Description: Controller used for operating product.
    :param browser: Browser instance for controller and components to share.
    :type browser: webdriver
    :param base_url: Base url for controller to operate off of.
    :type base_url: string
    """
    def __init__(self, browser, base_url):
        super(Product, self).__init__(browser, base_url, {
            'page': Page,
        })
