from selenium import webdriver


class WebDriver:
    """Main selenium web driver class"""

    def get_driver(self):
        """create instance of selenium web driver"""
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(options=options)
        return driver
