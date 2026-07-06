from pathlib import Path
from datetime import datetime

import pytest
from pytest_html import extras

from utils.driver_factory import create_driver
from utils.logger import get_logger


logger = get_logger(__name__)


@pytest.fixture
def driver(request):
    driver_instance = create_driver()
    request.node.driver = driver_instance
    logger.info("Browser started for test: %s", request.node.name)
    yield driver_instance
    logger.info("Browser closed for test: %s", request.node.name)
    driver_instance.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver_instance = getattr(item, "driver", None)
    if driver_instance is None:
        return

    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = screenshots_dir / f"{item.name}_{timestamp}.png"
    driver_instance.save_screenshot(str(screenshot_path))
    logger.error("Screenshot saved after failure: %s", screenshot_path)

    html_plugin = item.config.pluginmanager.getplugin("html")
    if html_plugin:
        report_extras = getattr(report, "extras", [])
        report_extras.append(extras.image(str(screenshot_path)))
        report.extras = report_extras
