import allure

from sprint_6_tests.locators.main_page_locators import MainPageLocators

class TestHeaderPage:
    @allure.title('Проверка нажатия на логотип Самоката.')
    def test_click_scooter_logo(self, header_page, main_page):
        main_page.click_order_button(True)
        header_page.click_scooter()
        assert main_page.find_element_with_wait(MainPageLocators.ORDER_BUTTON_MAIN)
