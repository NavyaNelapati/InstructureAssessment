import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from InstructureAssessment.config import Config

logger = logging.getLogger(__name__)


class WebDriverFactory:

    @staticmethod
    def get_driver(browser=None, headless=None):
        """
        Returns a WebDriver instance based on the specified browser and headless mode.

        Args:
            browser (str, optional): The browser to use for the WebDriver. Defaults to the value of Config.BROWSER.
                                     Supported values are "chrome" and "safari".
            headless (bool, optional): Whether to run the browser in headless mode. Defaults to the value of Config.HEADLESS.

        Returns:
            WebDriver: An instance of the WebDriver for the specified browser.

        Raises:
            ValueError: If the specified browser is not supported.
        """
        headless = headless or Config.HEADLESS
        browser = browser or Config.BROWSER

        if browser == "chrome":
            return WebDriverFactory._get_chrome_driver(headless)
        elif browser == "safari":
            return WebDriverFactory._get_safari_driver()
        else:
            raise ValueError("Unsupported Browser")

    @staticmethod
    def _get_chrome_driver(headless):
        """Returns an instance of Chrome WebDriver using WebDriverManager"""
        options = webdriver.ChromeOptions()
        logger.info(f"Running tests in headless mode: {headless}")

        if headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )
        return driver

    @staticmethod
    def _get_safari_driver():
        """Returns an instance of Safari WebDriver using WebDriverManager"""
        raise NotImplementedError("Safari WebDriver is not implemented yet")
