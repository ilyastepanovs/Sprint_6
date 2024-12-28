import allure


class TestHeaderPage:
    @allure.title('Проверка нажатия на логотип Самоката.')
    def test_click_scooter_logo(self, header_page, main_page):
        main_page.click_order_button(True)
        header_page.click_scooter()
        assert main_page.is_order_button_visible()
