import allure

from sprint_6_tests.locators.header_page_locators import HeaderPageLocators
from sprint_6_tests.pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Кликаем на логотип Самоката')
    def click_scooter(self):
        self.click_on_element(HeaderPageLocators.SCOOTER_LOGO)

    @allure.step('Кликаем на логотип Яндекса')
    def click_yandex(self):
        self.click_on_element(HeaderPageLocators.YANDEX_LOGO)