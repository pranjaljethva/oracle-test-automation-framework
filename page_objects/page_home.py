import time

from playwright.sync_api import Page
from locators import home_page_locators


class HomePage:

    def __init__(self, browser_page: Page):
        self.page = browser_page

    def open_navmenu(self):
        self.page.locator(home_page_locators.HOME_NAVIGATOR_MENU).wait_for(state="visible", timeout=10000)
        self.page.locator(home_page_locators.HOME_NAVIGATOR_MENU).click()

    def expand_parent_menu(self, menu_name):
        arrow_element = self.page.locator(home_page_locators.MENU_ARROW.format(menu_name))
        if arrow_element.get_attribute("title").__contains__("Expand"):
            time.sleep(1)
            locator = home_page_locators.MENU_LABEL.format(menu_name)
            self.page.locator(locator).wait_for(state="visible", timeout=5000)
            self.page.locator(locator).click()
            time.sleep(2)
            # self.page.locator(locator).click()
            # time.sleep(2)
            # self.page.locator(home_page_locators.MENU_CLOSE).click()
            # time.sleep(2)

    def display_submenu(self, submenu_name):
        print("Checking if " + submenu_name + " is displayed")
        return self.page.locator(home_page_locators.SUB_MENU_TITLE.format(submenu_name)).first.is_visible()

    def open_menu_tab(self, sub_title, main_title):
        self.page.locator(home_page_locators.MAIN_MENU_TITLE.format(main_title)).wait_for(state="visible",
                                                                                          timeout=10000)
        self.page.locator(home_page_locators.MAIN_MENU_TITLE.format(main_title)).click()
        self.page.locator(home_page_locators.MAIN_MENU_SUBTITLE.format(sub_title)).wait_for(state="visible",
                                                                                            timeout=10000)
        self.page.locator(home_page_locators.MAIN_MENU_SUBTITLE.format(sub_title)).click()
        self.page.locator(home_page_locators.PAGE_HEADING).wait_for(state="visible", timeout=20000)

    def is_page_displayed(self, page_name) -> bool:
        return self.page.locator(home_page_locators.PAGE_HEADING).is_visible(timeout=20000)