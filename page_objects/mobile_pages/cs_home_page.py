import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from common.element_helper import ElementHelper
from locators.mobile_locators import cs_login_locators as csll, cs_home_locators as cshl


class CSHomePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.element_helper = ElementHelper(self.driver)

    def verify_home_page_displayed(self):
        try:
            # is_displayed = self.element_helper.element_is_displayed(cshl.TXT_SAMSUNG_PASS)
            # if is_displayed:
            #     time.sleep(5)
            #     self.element_helper.get_element(cshl.CANCEL_BTN).click()
            #     self.element_helper.wait_for_invisibility_of_element_located(cshl.TXT_SAMSUNG_PASS)

            is_displayed = self.element_helper.element_is_displayed(cshl.NOTIFY_ALLOW)
            if is_displayed:
                print ("Notify window is displayed")
                self.element_helper.get_element(cshl.ALLOW_BTN).click()
                # self.element_helper.wait_for_invisibility_of_element_located(cshl.NOTIFY_ALLOW)

            is_displayed = self.element_helper.element_is_displayed(cshl.WELCOME_POPUP_MSG)
            if is_displayed:
                # time.sleep(5)
                self.element_helper.get_element(cshl.WELCOME_SKIP_BTN).click()
                # self.element_helper.wait_for_invisibility_of_element_located(cshl.WELCOME_POPUP_MSG)
                # time.sleep(5)
                return True
            else:
                return False

        except Exception as e:
            print("Error occurred while checking if homepage is displayed, " + str(e))
            return False

    def has_lock_icon(self, tab_name: str) -> bool:
        btn_locator = cshl.TEXT_CONTAINER.format(tab_name.upper())
        if not self.element_helper.element_is_displayed(btn_locator, 3):
            self.element_helper.scroll_in_window(50, 300, width=900, height=0, direction='right')
        locator = cshl.LOCK_BTN.format(tab_name.upper())
        return self.element_helper.element_is_displayed(locator, 3)

    def open_global_feed(self):
        is_displayed = self.element_helper.element_is_displayed(cshl.NAVBAR_BTN)
        if is_displayed:
            self.element_helper.get_element(cshl.NAVBAR_BTN).click()
            displayed = self.element_helper.element_is_displayed(cshl.GLOBAL_FEED)
            if displayed:
                self.element_helper.get_element(cshl.GLOBAL_FEED).click()

    def open_tab(self, tab_name: str):
        is_displayed = self.element_helper.element_is_displayed(cshl.TEXT_CONTAINER.format(tab_name.upper()))
        if is_displayed:
            self.element_helper.get_element(cshl.TEXT_CONTAINER.format(tab_name.upper())).click()
            time.sleep(3)

    def verify_report_type_found(self, expected_type):

        report_types = self.element_helper.get_element_list(cshl.TEXT_REPORT_TYPE.format(expected_type))
        counter = 0
        rect = self.element_helper.get_element(cshl.DIV_CONTENT).rect
        print("left = " + str(rect['x']))
        print("top = " + str(rect['y']))
        print("width = " + str(rect['width']))
        print("height = " + str(rect['height']))

        while len(report_types) == 0:

            left = rect['x'] + 100
            top = rect['y'] + 100
            width = left
            height = 1200

            self.element_helper.scroll_in_window(left, top, width, height, "down")
            report_types = self.element_helper.get_element_list(cshl.TEXT_REPORT_TYPE.format(expected_type))

            print(counter)
            counter += 1
            if counter > 15:
                break

        return len(report_types) > 0

    def verify_one_report_type(self, expected_type):
        report_types = self.element_helper.get_element_list(cshl.TEXT_REPORT_TYPE.format(expected_type), 4)
        counter = 0
        rect = self.element_helper.get_element(cshl.DIV_CONTENT).rect
        print("left = " + str(rect['x']))
        print("top = " + str(rect['y']))
        print("width = " + str(rect['width']))
        print("height = " + str(rect['height']))

        result = False
        while counter < 5:
            left = rect['x'] + 100
            top = rect['y'] + 100
            width = left
            height = 1200

            self.element_helper.scroll_in_window(left, top, width, height, "down")
            report_types = self.element_helper.get_element_list(cshl.TEXT_REPORT_TYPE.format(expected_type), 3)

            for element in report_types:
                actual_type = element.text
                result = actual_type.lower().__eq__(expected_type.lower())
                if not result:
                    break
                # if actual_type != expected_type:
                #     raise AssertionError("Expected only " + expected_type + "reports but found "
                #                          + actual_type + "after scroll")
            if not result:
                break
            counter += 1
        return result

