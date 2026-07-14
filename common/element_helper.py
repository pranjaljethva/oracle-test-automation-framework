from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from support.config_reader import ConfigReader

class ElementHelper():

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.driver.implicitly_wait(time_to_wait=10)
        self.wait = WebDriverWait(driver=driver, timeout=10)
        self.config_reader = ConfigReader()

    def element_is_displayed(self, locator: str, timeout = None) -> bool:
        try:
            if timeout is not None:
                self.driver.implicitly_wait(time_to_wait=timeout)
                self.wait = WebDriverWait(driver=self.driver, timeout=timeout)

            element = self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, locator)))
            if element:
                return True
            return False
        except Exception as e:
            print("Exception while trying to wait for the element by locator " + locator + " to visible. " + str(e))
            return False
        finally:
            self.driver.implicitly_wait(time_to_wait= self.config_reader.get_base_config_value("default_implicit_wait"))
            self.wait = WebDriverWait(driver=self.driver,
                                      timeout=self.config_reader.get_base_config_value("default_explicit_wait"))

    def wait_for_invisibility_of_element_located(self, locator: str) -> bool:
        try:
            result = self.wait.until(EC.invisibility_of_element_located((AppiumBy.XPATH, locator)))
            return True if result else False
        except Exception as e:
            print("Exception while trying to wait for the element to visible. " + str(e))
            raise e

    def get_element(self, locator: str):
        try:
            # element = self.driver.find_element(AppiumBy.XPATH, locator)
            element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, locator)))
            return element
        except Exception as e:
            print("Exception while trying to get element. " + str(e))
            raise e

    def get_element_list(self, locator: str, timeout = None):
        try:
            if timeout is not None:
                self.driver.implicitly_wait(time_to_wait=timeout)
                self.wait = WebDriverWait(driver=self.driver, timeout=timeout)

            elements = self.driver.find_elements(AppiumBy.XPATH, locator)
            return elements
        except Exception as e:
            print("Exception while trying to get element. " + str(e))
            raise e

        finally:
            self.driver.implicitly_wait(time_to_wait= self.config_reader.get_base_config_value("default_implicit_wait"))
            self.wait = WebDriverWait(driver=self.driver,
                                      timeout=self.config_reader.get_base_config_value("default_explicit_wait"))


    def scroll_to_text(self, text):
        """Scrolls a scrollable container until an element with the given text is visible."""
        selector = (
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{text}"))'
        )
        print ("My selector is : " + selector)
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)

    def scroll_in_window(self,
                        left: int, top: int,
                         width: int, height: int,
                         direction : str, percent: float = "1.0"):
        self.driver.execute_script('mobile: scrollGesture', {
            'left': left, 'top': top, 'width': width, 'height': height,
            'direction': direction,
            'percent': percent
        })

