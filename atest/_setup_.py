from library.qat.todo.controller import Emc


class Setup():

    def setup_func(self, driver):
        """
        :Description: Shared setup function. Usually where you spin the driver (for this suite we are always going to
        use chrome with no arguments. Normally there would be another param just for arguments.
        :param driver: This is where the webdriver is passed in. Usually this would be determined with some sort on env
        var.
        :type driver: Selenium Webdriver object
        """
        controller = Emc(driver, "https://www.emersonecologics.com/")
        return controller
