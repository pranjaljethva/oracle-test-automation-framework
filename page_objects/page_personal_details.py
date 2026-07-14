import time

from locators import personal_details_locators as pd_locators
from playwright.sync_api import Page, expect


class PersonalDetailsPage:

    def __init__(self, page: Page):
        self.page = page

    def search_employee(self, employee_id):
        self.page.locator(pd_locators.SEARCH_EMPLOYEE).click()
        self.page.locator(pd_locators.SEARCH_EMPLOYEE).fill(employee_id)
        self.page.locator(pd_locators.SEARCH_RESULTS).first.wait_for(state="visible", timeout=10000)
        # self.page.locator(personal_details_locators.SEARCH_RESULTS).first.click()
        # time.sleep(1)
        self.page.locator(pd_locators.SEARCH_RESULTS).press("Enter")
        # time.sleep(3)

    def verify_employee_page(self, employee_name) -> bool:
        self.page.locator(pd_locators.PAGE_OF_EMPLOYEE.format(employee_name)).wait_for(state="visible",
                                                                                       timeout=10000)
        result = self.page.locator(pd_locators.PAGE_OF_EMPLOYEE.format(employee_name)).is_visible()
        return result

    def verify_page_load(self) -> bool:
        self.page.locator(pd_locators.LABEL_EDU_LEVEL).wait_for(state="visible", timeout=20000)
        result = self.page.locator(pd_locators.LABEL_EDU_LEVEL).is_visible()
        return result

    def click_edit_dmg(self):
        self.page.locator(pd_locators.EDIT_BUTTON).last.click()
        self.page.locator(pd_locators.PERSONAL_DMG_INPUT).first.wait_for(state="visible", timeout=20000)
        time.sleep(2)

    def enter_fields(self, field_label: str, field_value: str):
        temp_label = field_label.replace(" ", "")
        input_selector = self.page.locator(pd_locators.COMBOBOX_SELECTOR.format(temp_label))
        if input_selector.is_visible(timeout=5000):
            input_selector.click()

        input_locator = self.page.locator(pd_locators.INPUT_FIELDS.format(field_label))
        # input_locator.click()
        # time.sleep(3)
        att_role = input_locator.get_attribute("role")

        if att_role and att_role.lower().__eq__("combobox"):
            # input_locator.click()
            self.page.locator(pd_locators.COMBOBOX_LIST_NEW.format(temp_label)).wait_for(state="visible", timeout=10000)
            # self.page.locator(pd_locators.COMBOBOX_LIST).first.wait_for(state="visible", timeout=10000)
            # self.page.locator(pd_locators.COMBOBOX_ITEM.format(field_value)).first.click()
            self.page.locator(pd_locators.COMBOBOX_ITEM_NEW.format(field_value)).click()
            expect(input_locator).to_have_value(field_value, timeout=10000)
            time.sleep(2)
        else:
            input_locator.click()
            input_locator.clear(force=True)
            input_locator.fill(field_value)
            time.sleep(2)

    def save_modified_section(self):
        self.page.locator(pd_locators.SAVE_BUTTON).wait_for(state="visible",timeout=5000)
        self.page.locator(pd_locators.SAVE_BUTTON).click()
        time.sleep(5)
        expect(self.page.locator(pd_locators.SHOW_DMG_LINK)).not_to_have_class("oj-disabled", timeout=20000)
        print("the link is displayed")

    def verify_dmg_info(self,field_label: str, field_value: str):

        field_locator = self.page.locator(pd_locators.UPDATED_FIELD.format(field_label, field_label)).last

        field_tag: str = field_locator.evaluate("element => element.tagName")
        if field_tag.__eq__("DIV"):
            expect(field_locator).not_to_be_empty(timeout=10000)
            print("Div field text is: " + field_locator.text_content())
            return field_locator.text_content()
        elif field_tag.__eq__("INPUT"):
            eye_locator = self.page.locator(pd_locators.EYE_BUTTON.format(field_label))
            if eye_locator.is_visible(timeout=5000):
                if str(eye_locator.get_attribute("aria-checked")).lower().__eq__("true"):
                    eye_locator.click()
                    expect(eye_locator).to_have_attribute("aria-checked", "false")
                    time.sleep(2)
            print("Input field text is: " + field_locator.input_value())
            return field_locator.input_value()


