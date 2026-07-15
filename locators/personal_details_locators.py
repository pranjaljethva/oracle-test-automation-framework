SEARCH_EMPLOYEE = "//div[contains(@id,'searchInput')]//input"
PAGE_OF_EMPLOYEE = "//div[contains(@id,'personal-details')][@title = '{}']"

SEARCH_SUGGESTIONS = "//*[contains(@id, 'searchSuggestionsListbox')]"
SEARCH_RESULTS = "//*[contains(@id, 'searchSuggestionsListbox')]//div[@role='option']"

COUNTRY_OF_DMG = "//div[contains(@aria-labelledby, 'person-dmg-info-leg-read')][text()='{}']"
LABEL_EDU_LEVEL = "//label[text()='Highest Education Level']"
EDIT_BUTTON = "//button[contains(@aria-label,'Edit Demographic info')]"
PERSONAL_DMG_INPUT = "//label[contains(@id,'person-dmg-info')]//span[text()='Religion']"

INPUT_FIELDS = "//oj-input-text//span[text()='{}']/ancestor::oj-label/following-sibling::input"
COMBOBOX_LIST = "//ul[contains(@aria-labelledby, 'person-dmg-info-leg-edit')]"
COMBOBOX_LIST_NEW = "oj-list-view[id*='{}']"
COMBOBOX_ITEM = "//ul[contains(@aria-labelledby, 'person-dmg-info-leg-edit')]//span[text()= '{}']"
COMBOBOX_ITEM_NEW = "//li[contains(@class, 'oj-listview-focused-element')]//span[text()= '{}']"
COMBOBOX_SELECTOR = "oj-select-single[id*='{}']"

SAVE_BUTTON = "//span[text()='Save']/ancestor::oj-button[1]"
SHOW_DMG_LINK = "//a[text()='Show Prior Demographic Info']"

UPDATED_FIELD = "//label[text()='{}']/following-sibling::div[1] | //label[text()='{}']/following-sibling::input"

EYE_BUTTON = "//label[text()='{}']/../following-sibling::span//button[@aria-label='Sensitive text hidden']"
