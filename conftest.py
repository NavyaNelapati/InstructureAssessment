import logging
import os
import time
import traceback
import datetime

import pytest

from utils.webdriver_factory import WebDriverFactory

# Create required directories

logger = logging.getLogger(__name__)  # Get global logger


def pytest_addoption(parser):
    parser.addoption(
        "--screenshot-dir",
        action="store",
        default="screenshots",
        help="screenshots directory",
    )
    parser.addoption(
        "--logs-dir", action="store", default="logs", help="logs directory"
    )
    parser.addoption(
        "--reports-dir", action="store", default="reports", help="report directory"
    )


def pytest_configure(config):
    screenshot_dir = config.getoption("--screenshot-dir")
    logs_dir = config.getoption("--logs-dir")
    reports_dir = config.getoption("--reports-dir")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create screenshots directory if it doesn't exist
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # Create reports directory if it doesn't exist
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Run pytest with HTML reporting
    report_path = config.getoption("--html")
    if not report_path:
        config.option.htmlpath = f"{reports_dir}/report_{timestamp}.html"
        
    logfile_path = config.getoption("--log-file")
    if not logfile_path:
        config.option.log_file = f"{logs_dir}/log_{timestamp}.log"


@pytest.fixture(scope="session")
def driver():
    """Fixture to set up WebDriver and return it for test execution."""
    driver = WebDriverFactory.get_driver()
    logger.info("Browser started for test execution.")
    yield driver

    driver.quit()
    logger.info("Browser closed after test execution.")


def pytest_runtest_makereport(item, call):
    """Capture screenshots and log errors on test failure."""
    if call.when == "call" and call.excinfo is not None:  # If test fails
        test_name = item.nodeid.split("::")[-1]  # Get test function name
        screenshot_dir = item.config.getoption("--screenshot-dir", None)
        if screenshot_dir:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = os.path.join(
                screenshot_dir, f"{test_name}_{timestamp}.png"
            )
            logger.info(f"Capturing screenshot: {screenshot_path}")
            driver = item.funcargs["driver"]  # Access WebDriver
            driver.save_screenshot(screenshot_path)

        # Capture exception and traceback
        error_message = str(call.excinfo.value)  # Get error message
        traceback_info = "".join(
            traceback.format_exception(None, call.excinfo.value, call.excinfo.tb)
        )

        # Log error details
        logger.error(f"Test failed: {test_name}")
        logger.error(f"Error message: {error_message}")
        logger.error(f"Traceback:\n{traceback_info}")
