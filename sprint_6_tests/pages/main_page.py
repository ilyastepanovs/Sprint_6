import allure
from sprint_6_tests.locators.main_page_locators import MainPageLocators
from sprint_6_tests.pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Кликаем на вопрос и получаем текст ответа')
    def click_question_and_get_answer_text(self, num):
        method, locator = MainPageLocators.QUESTION_LOCATOR
        locator_question = locator.format(num)
        self.scroll_to_element((method, locator_question))
        self.click_on_element((method, locator_question))
        method, locator = MainPageLocators.ANSWER_LOCATOR
        locator_answer = locator.format(num)
        return self.get_text_from_element((method, locator_answer))

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_order_button(self, is_header_button):
        if is_header_button:
            self.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER)
        else:
            self.click_on_element(MainPageLocators.ORDER_BUTTON_MAIN)

    @allure.step('Проверяем видимость кнопки "Заказать"')
    def is_order_button_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_BUTTON_MAIN)
