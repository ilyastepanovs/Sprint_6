import allure
import pytest
import datetime


class TestOrderPage:
    @allure.title('Проверка позитивного сценария заказа самоката.')
    @pytest.mark.parametrize("is_header_button, name, surname, address, metro, phone, delivery_date, rent_period",
                             [ (True, 'Иванов', 'Иван', 'ул. Никольская, д. 12', 'Сокольники', '89101112233',
                                datetime.date.today().day, 'сутки'),
                               (False, 'Александр', 'Александров', 'ул. Архангельская, д. 3', 'Кузьминки', '89880009977',
                                datetime.date.today().day, 'трое суток')]
                             )
    def test_scooter_order_true(self, main_page, order_page, is_header_button, name, surname,
                                address, metro, phone, delivery_date, rent_period):
        main_page.click_order_button(is_header_button)
        order_page.for_who_form(name, surname, address, metro, phone)
        order_page.about_rent_form(delivery_date, rent_period)
        assert 'Заказ оформлен' in order_page.check_order()
