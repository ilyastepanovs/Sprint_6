import allure

from sprint_6_tests.locators.dzen_page_locators import DzenPageLocators
from sprint_6_tests.pages.base_page import BasePage


class DzenPage(BasePage):
    @allure.step('Проверяем, что открылась страница Дзена')
    def dzen_page_opened(self):
        self.move_to_next_tab()
        return self.get_text_from_element(DzenPageLocators.DZEN_SEARCH_BUTTON)
