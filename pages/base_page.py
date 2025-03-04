"""
Base page class with common methods for all page objects.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
)

from config import Config


class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver, timeout=None):
        """
        Initialize the base page.

        Args:
            driver: WebDriver instance
            timeout (int): Default timeout for waiting operations
        """
        self.driver = driver
        self.timeout = timeout or Config.EXPLICIT_WAIT

    def navigate_to(self, url):
        """Navigate to the specified URL."""
        self.driver.get(url)

    def wait_for_element_visible(self, locator):
        """
        Wait for an element to be visible.

        Args:
            locator (tuple): Element locator (By strategy, selector)

        Returns:
            WebElement: The found element

        Raises:
            TimeoutException: If the element is not visible within the timeout
        """
        wait = WebDriverWait(
            self.driver,
            self.timeout,
            ignored_exceptions=[StaleElementReferenceException],
        )
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        """
        Wait for an element to be clickable.

        Args:
            locator (tuple): Element locator (By strategy, selector)

        Returns:
            WebElement: The found element

        Raises:
            TimeoutException: If the element is not clickable within the timeout
        """
        wait = WebDriverWait(
            self.driver,
            self.timeout,
            ignored_exceptions=[StaleElementReferenceException],
        )
        return wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        """
        Wait for an element to be clickable and then click it.

        Args:
            locator (tuple): Element locator (By strategy, selector)

        Returns:
            WebElement: The clicked element

        Raises:
            TimeoutException: If the element is not clickable within the timeout
        """
        web_element = self.wait_for_element_clickable(locator)
        web_element.click()
        return web_element

    def fill_text_field(self, locator, text):
        """
        Fill a text field with the specified text.

        Args:
            locator (tuple): Element locator (By strategy, selector)
            text (str): Text to enter into the field

        Returns:
            WebElement: The text field element

        Raises:
            TimeoutException: If the element is not visible within the timeout
        """
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)
        return element

    def get_element_text(self, locator):
        """
        Get the text of an element.

        Args:
            locator (tuple): Element locator (By strategy, selector)

        Returns:
            str: The text of the element

        Raises:
            TimeoutException: If the element is not visible within the timeout
        """
        element = self.wait_for_element_visible(locator)
        return element.text

    def is_element_displayed(self, locator, timeout=None):
        """
        Check if an element is displayed.

        Args:
            locator (tuple): Element locator (By strategy, selector)
            timeout (int, optional): Custom timeout for this operation

        Returns:
            bool: True if the element is displayed, False otherwise
        """
        timeout = timeout if timeout is not None else self.timeout
        try:
            wait = WebDriverWait(
                self.driver,
                timeout,
                ignored_exceptions=[StaleElementReferenceException],
            )
            return wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_for_url_contains(self, text, timeout=None):
        """
        Wait for the URL to contain specific text.

        Args:
            text (str): Text to check for in the URL
            timeout (int, optional): Custom timeout for this operation

        Returns:
            bool: True if the URL contains the text, False otherwise
        """
        timeout = timeout if timeout is not None else self.timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.url_contains(text))
        except TimeoutException:
            return False

    def wait_for_page_load(self, timeout=None):
        """Wait for the page to fully load based on document.readyState."""
        timeout = timeout or Config.IMPLICIT_PAGE_TIMEOUT
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            lambda driver: driver.execute_script("return document.readyState")
            == "complete"
        )

    def scroll_to_element(self, locator):
        """Scroll element into view"""
        web_element = self.wait_for_element_visible(locator)
        if web_element.is_displayed():
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'end'});", web_element
            )
        return web_element
