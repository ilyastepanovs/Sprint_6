import allure

from sprint_6_tests.locators.order_page_locators import OrderPageLocators
from sprint_6_tests.pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Выбираем станцию метро из выпадающего списка')
    def select_metro_station(self, station):
        method, locator = OrderPageLocators.METRO_STATION
        metro_locator = locator.format(station)
        self.click_on_element(OrderPageLocators.METRO_INPUT)
        self.scroll_to_element((method, metro_locator))
        self.click_on_element((method, metro_locator))

    @allure.step('Выбираем дату в календаре')
    def select_date_from_calendar(self, date):
        method, locator = OrderPageLocators.CALENDAR_INPUT
        date = locator.format(date)
        self.click_on_element(OrderPageLocators.DELIVERY_DATE)
        self.click_on_element((method, date))

    @allure.step('Выбираем период из выпадающего списка')
    def select_rent_period(self, rent_period):
        method, locator = OrderPageLocators.RENT_PERIOD_DROPDOWN
        period = locator.format(rent_period)
        self.click_on_element(OrderPageLocators.RENT_PERIOD)
        self.scroll_to_element((method, period))
        self.click_on_element((method, period))

    @allure.step('Заполняем форму "Для кого самокат"')
    def for_who_form(self, name, surname, address, metro, phone):
        self.find_element_with_wait(OrderPageLocators.FOR_WHO_TITLE)
        self.set_text_to_element(OrderPageLocators.NAME_INPUT, name)
        self.set_text_to_element(OrderPageLocators.SURNAME_INPUT, surname)
        self.set_text_to_element(OrderPageLocators.ADDRESS_INPUT, address)
        self.select_metro_station(metro)
        self.set_text_to_element(OrderPageLocators.TELEPHONE_INPUT, phone)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем форму "Про аренду"')
    def about_rent_form(self, delivery_date, rent_period):
        self.find_element_with_wait(OrderPageLocators.ABOUT_RENT_TITLE)
        self.select_date_from_calendar(delivery_date)
        self.select_rent_period(rent_period)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Проверяем успешность заказа')
    def check_order(self):
        self.click_on_element(OrderPageLocators.YES_BUTTON)
        success_result = self.get_text_from_element(OrderPageLocators.ORDER_PLACED_TITLE)
        self.click_on_element(OrderPageLocators.SHOW_STATUS_BUTTON)
        return success_result

