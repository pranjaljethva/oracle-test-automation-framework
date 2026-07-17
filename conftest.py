import os
from datetime import datetime
from typing import Dict

import allure
import pytest
import pytest_html.extras
from appium.options.common import AppiumOptions
from pytest_bdd import given, when, then, step
from playwright.sync_api import sync_playwright, Page
import sys
from pathlib import Path

from appium import webdriver as mobile_driver

from pytest_bdd.parser import Scenario

from common import common_config
from support.config_reader import ConfigReader

# Add steps directory to path to ensure imports work
steps_dir = Path(__file__).parent / "steps"
if str(steps_dir) not in sys.path:
    sys.path.insert(0, str(steps_dir))


@pytest.fixture()
def browser():
    with sync_playwright() as p:
        browser_instance = p.chromium.launch(
            headless=False,
            args=['--start-maximized'])
        context = browser_instance.new_context(no_viewport=True)
        page = context.new_page()
        my_page = page
        yield page
        browser_instance.close()

@pytest.fixture()
def mbl_application():
    config_reader = ConfigReader()
    project_path = config_reader.get_project_path()

    options = AppiumOptions()
    capabilities = {}
    device = config_reader.get_base_config_value("device")
    device_caps: Dict = config_reader.get_base_config_value("devices")[device]

    application = config_reader.get_base_config_value("mobile_app_name")
    app_caps: Dict = config_reader.get_base_config_value("mobile_app_capabilities")[application]

    for key in device_caps.keys():
        capabilities[key] = device_caps.get(key)

    for key in app_caps.keys():
        if str(key).__eq__("app") or str(key).__eq__("appium:app"):
            abs_path = project_path + os.sep + app_caps[key]
            capabilities[key] = abs_path
        else:
            capabilities[key] = app_caps.get(key)

    options.load_capabilities(capabilities)

    driver = mobile_driver.Remote("http://127.0.0.1:4723", options=options)
    yield driver

def pytest_configure():
    config_reader = ConfigReader()
    project_path = config_reader.get_project_path()
    screenshot_path = project_path + os.sep + "reports" + os.sep + "screenshots" + os.sep
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)
    else:
        common_config.delete_all_files(screenshot_path)

    allure_path = project_path + os.sep + "reports" + os.sep + "allurereport"
    common_config.delete_all_files(allure_path)


def pytest_bdd_after_scenario(request, scenario : Scenario):
    config_reader = ConfigReader()
    project_path = config_reader.get_project_path()

    if "web_ui" in scenario.tags:
        screenshot_path = project_path + os.sep + "reports" + os.sep + "screenshots" + os.sep
        screenshot_name = scenario.name[:10] + datetime.now().strftime("%d%m%Y%H%M%S.png")
        screenshot_name = screenshot_name.replace(" ", "_")
        page: Page = request.getfixturevalue("browser")
        page.screenshot(timeout=10000, full_page=True, path=screenshot_path + screenshot_name)

        allure.attach.file(screenshot_path + screenshot_name, name=screenshot_name, attachment_type=allure.attachment_type.JPG)


